# Python 爬虫练习
爬取百度百科 python 词条 1000个

## 环境
python3

### 依赖
    pip install beautifulsoup4

### 运行
    python spider_main.py

如果爬取不了，则百度修改了页面，根据页面修改爬取规则（ html_parser.py 修改规则）

* spider_main 爬虫总调度程序
* url_manager url 管理器
* html_downloader html 下载器
* html_parser html 解析器
* html_outputer 输出
