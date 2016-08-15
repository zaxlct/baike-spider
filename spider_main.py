## -*- coding: utf-8 -*-
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    # 爬虫总调度程序会使用 url 管理器、 html 的下载器、解析器、输出器，下面初始化一下：
    def __init__(self):
        self.urls = url_manager.url_Manager()
        self.download = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        pass

if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/view/21087.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) # 启动爬虫
