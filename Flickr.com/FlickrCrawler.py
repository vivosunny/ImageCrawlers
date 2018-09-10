import requests

import Categories
import logging

import os
import time

from tqdm import tqdm


# logging.basicConfig(level=logging.DEBUG)


class FlickrCrawler:
    def __init__(self, result_path, item):
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://api.flickr.com/services/rest/"
        self.headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
        }
        # self.time_split = "2013-12-31 23:59:59"
        self.time_split = "1262318400" # Unix Timestamp 2010-1-1
        self.request_parameter = {
            "format": "json",
            "method": "flickr.photos.search",
            "api_key": "fc6930bfb896b7cd7ad53dd1e258b486",
            "nojsoncallback": "1",
            "text": item['keyword'],
            "extras": 'url_o, url_k, url_h, url_b',
            "page": 1,
            # "min_upload_date": "2016-01-31 23:59:59",
            # "max_upload_date": "2016-01-31 23:59:59",
            "sort": "relevance"
        }

        # 文件夹地址
        # self.root = self.__init_folder()

        # 指定结果路径爬取
        self.result_path = result_path
        self.item_info = item

        self.multiple = 4

        if 'multiple' in self.item_info.keys():
            self.multiple = 4 * self.item_info['multiple']

    def walk(self):
        # category_path = self.make_category_path(self.root, keyword)
        keyword = self.item_info['keyword']
        self.request_parameter['text'] = keyword

        with open(os.path.join(self.result_path, 'urls.txt'), 'w') as file:
            if self.item_info['num'] > 0:
                total, pic_count = self.__get_photo(1, file)
                self.logger.info('Found %d pics in category: %s' % (total, keyword))
                total_page = 2
                page = 2

                with tqdm(total=self.item_info['num'] * self.multiple, leave=False, desc=keyword) as pbar:
                    while page <= total_page and pic_count <= self.multiple * self.item_info['num']:
                        total_page, count = self.__get_photo(page, file)
                        pic_count += count
                        pbar.update(count)
                        page += 1

    def __get_photo(self, page, file):
        self.request_parameter['page'] = page
        if self.item_info['num'] * self.multiple >= 4000:
            if page == 1:
                # 错开时间搜索
                if 'max_upload_date' in self.request_parameter.keys():
                    del self.request_parameter['max_upload_date']
                self.request_parameter['min_upload_date'] = self.time_split
            if page == 40:
                if 'min_upload_date' in self.request_parameter.keys():
                    del self.request_parameter['min_upload_date']
                self.request_parameter['max_upload_date'] = self.time_split
            if page >= 40:
                # 从第一页开始
                self.request_parameter['page'] = page - 39
        photos = self.__get_photos()
        valid_photos = 0
        '''
            Flickr 照片大小命名规则：
            s 小正方形 75x75
            q 大正方形 150x150
            t 缩图，最长边为 100
            m 小图，最长边为 240
            n 小图，最长边为 320
            - 中图，最长边为 500
            z 中图，最长边为 640
            c 中图，最长边为 800†
            b 大图，最长边为 1024*
            h 大图，最长边为 1600†
            k 大图，最长边为 2048†
            o 原始图片，根据来源格式可以是 jpg、gif 或 png

            * 2010 年 5 月 25 日之前，大相片仅适用于特别大的原始图片。
            † 中型 800、大型 1600 和大型 2048 相片仅存在于 2012 年 3 月 1 日之后。
        '''
        url_lines = []
        for photo in photos['photo']:
            image_url = ''
            if 'url_o' in photo.keys():
                image_url = photo['url_o']
            elif 'url_k' in photo.keys():
                image_url = photo['url_k']
            elif 'url_h' in photo.keys():
                image_url = photo['url_h']
            elif 'url_b' in photo.keys():
                image_url = photo['url_b']

            if image_url is not '':
                valid_photos += 1
                url_lines.append(image_url + '\n')
            # else:
            # self.logger.debug('No suitable size')

        file.writelines(url_lines)
        time.sleep(1)
        return int(photos['total']), valid_photos

    def __get_photos(self):
        response = requests.get(self.base_url,
                                headers=self.headers,
                                params=self.request_parameter)
        self.logger.debug(response.text)
        photos = response.json()['photos']
        return photos

    @classmethod
    def __init_folder(cls):
        """
        准备文件夹
        需要检测是否存在相同uid、不同name的情况
        :return: str 该用户的存储文件夹名
        """
        # 根目录
        root = Categories.STORE_PATH
        if not os.path.exists(root):
            os.mkdir(root)

        return root
