import re
from bs4 import BeautifulSoup
from urllib import parse


class HtmlParser(object):

    def parse(self, new_url, html_content):
        if html_content is None or new_url is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls,new_data

    def _get_new_urls(self, new_url, soup):
        full_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/"))
        for link in links:
            url_href = link["href"]
            full_url_href = parse.urljoin(new_url, url_href)
            full_urls.add(full_url_href)
        return full_urls

    def _get_new_data(self, new_url, soup):
        res_data = {"url": new_url}
        # 获取title class="lemmaWgt-lemmaTitle-title"
        title = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1").get_text()
        res_data["title"] = title
        # 获取摘要  class = "lemma-summary"
        summary = soup.find("div", class_="lemma-summary").get_text()
        res_data["summary"] = summary
        return res_data
