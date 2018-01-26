from baike_spider import url_manager, html_downer, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downer.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, begin_url):
        count = 1
        self.urls.add_new_url(begin_url)
        while self.urls.has_new_url():
            try:
                if count > 100:
                    break
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
            except BaseException as e:
                print(e)
                print("craw fail")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
