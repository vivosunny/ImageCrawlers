# Flickr 爬虫

## 使用方法

1. 修改 `Categories.py` 中的关键词数据

   - `keyword` 关键词
   - `name` 文件夹名，不指定的话默认为 `keyword` 
   - `num` 下载数量，将放大 4 倍下载，如指定为 100 则会下载 400 张图片，不指定的话默认为 50

2. 在 `Categories.py` 中指定下载路径

3. 运行

   ```bash
   # 安装依赖
   pip install -r requirements.txt
   python UrlFetcher.py 0 10
   ```

   其中 `0` 和 `10` 指定了关键词范围，为 `Categories.py` 中的数组索引值，左闭右开，如指定 `0` 到 `10` 会下载关键词数组的第 `1` 项（索引值为 `0` ）到第 `10` 项（索引值为 `9`）

## 注意事项

因为 `Flickr API` 会限制 `4000` 张以上的查询，当 `num` 值大于 `1000` 时会采用限定时间范围的方法获得图片 `url`。