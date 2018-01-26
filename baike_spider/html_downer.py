import ssl
from urllib import request


class HtmlDownloader(object):

    def download(self, new_url):
        ssl._create_default_https_context = ssl._create_unverified_context
        response = request.urlopen(new_url)
        print("请求返回码：%d" % response.getcode())
        if response.getcode() != 200:
            return None
        return response.read()

