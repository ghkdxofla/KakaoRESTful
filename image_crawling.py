'''
Date : 2018-09-28

Author: Hwang Taelim

Content: Module for crawling famous painting files
'''


import requests, json
from bs4 import BeautifulSoup
from urllib.parse import urlencode, quote_plus, unquote


class IMGCrawler(object):
    def __init__(self, url="http://www.abcgallery.com", headers=None):
        self.url = url
        if headers is None:
            self.headers = {'User-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        else:
            self.headers = headers

    def set_url(self, url):
        self.url = url

    def get_data(self, num_retries=5):
        with requests.Session() as s:
            s.keep_alive = False
            try:
                res = s.get(url=self.url, headers=self.headers, timeout=10)
                if 500 <= res.status_code < 600:
                    print(res.status_code, res, res.reason)
                    raise ConnectionError

            except Exception as e:
                s.close()
                print(e)
                print("--TRY CONNECTION {0}...--".format(num_retries))
                if num_retries > 0:
                    return self.get_data(num_retries=num_retries-1)
                else:
                    print("--MAX RETRY REACHED!--")
                    return None
            else:
                html = BeautifulSoup(res.content, 'lxml')
                lists = html.select('.row ul li')
                return lists


if __name__=="__main__":
    img_crawler = IMGCrawler()
