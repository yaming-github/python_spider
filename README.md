# 爬取虎扑评论并制作词云
## 第一步: 安装依赖
```
pip333 install -r requriements.txt
```

## 第二步: 爬取评论
```
python3 spider.py
```
评论写入'./comment.txt'文件中

## 第三步: 中文分词，制作词云
```
python3 cloud.py
```
生成的词云图片为'./word_cloud.jpg'
