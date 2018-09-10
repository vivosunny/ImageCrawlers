import os
import sys
import FlickrCrawler

import time

import Categories

from homura import download
from multiprocessing.dummy import Pool as ThreadPool


def make_category_path(root, category):
    """
    生成并创建相册下载路径
    :param root: 数据存储文件夹
    :param category: 相册数据
    :return: str 下载路径
    """
    category_path = os.path.join(root, category)
    print(category_path)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    return category_path


def make_category_path(path):
    """
    生成并创建相册下载路径
    :param path: 数据存储文件夹
    :return: str 下载路径
    """
    if not os.path.exists(path):
        os.makedirs(path)

    return path


def download_(lines):
	try:
		download(lines)
	except Exception as e:
		print(e)


def main():
    pool = ThreadPool(2)
    categories = Categories.CATEGORIES
    count = 1
    start_time_gl = time.clock()
    results_root = Categories.RESULTS_ROOT
    for scene in categories[int(sys.argv[1]):int(sys.argv[2])]:
        category_name = scene['name'].replace('\\', '/')
        if 'children' in scene.keys():
            required_num = 100
            if 'num' in scene.keys():
                required_num  = scene['num']
            for item in scene['children']:
                if not item.__contains__('name'):
                    item['name'] = item['keyword'].replace(' ', '_').lower()
                if not item.__contains__('num'):
                    item['num'] = required_num
                item_path = os.path.join(results_root , category_name, item['name'])
                if not os.path.exists(item_path):
                    os.makedirs(item_path)
                # 断点续传
                print(item)
                if not os.path.isfile(os.path.join(item_path , 'finished.txt')):
                    start_time = time.asctime(time.localtime(time.time()))
                    if item['num'] >= 0:
                        crawler = FlickrCrawler.FlickrCrawler(item_path, item)
                        crawler.walk()
                    # 只读文件
                    with open(os.path.join(item_path , 'urls.txt')) as urls:
                        os.chdir(item_path)
                        lines = urls.readlines()
                        lines_ = []

                        for line in lines:
                            lines_.append(line.strip('\n'))

                        pool.map(download_, lines_)
                    # 创建完成标志
                    with open(os.path.join(item_path , 'finished.txt'), 'w') as finish_flag_file:
                        finish_flag_file.write(start_time)
                        finish_flag_file.write(time.asctime(time.localtime(time.time())))
                else:
                    print(os.path.join(item_path , 'finished.txt'))

                count += 1

    pool.close()
    pool.join()

    print("end at", time.clock() - start_time_gl)


if '__main__' == __name__:
    main()
