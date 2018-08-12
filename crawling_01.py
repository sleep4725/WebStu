from bs4 import BeautifulSoup
import requests as req
from urllib.request import (urlopen, urlretrieve)
import os
import re
import pprint as ppr
import operator
#-----------------------------------------------------------
class Movie(object):
    def __init__(self):
        self.url  = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
        self.html = req.get(url=self.url)
        self.selector = {
            1:"#old_content > table > tbody > tr > td.title > div > a",
            2:"#content > div.article > div.mv_info_area > div.poster > a > img"
        }
        self.filtering_one = re.compile("&")
        self.filtering_two = re.compile(".jpg")
        self.movDict   = dict() # dictionary

    def url_request(self):
        if self.html.ok:
            bsObject = BeautifulSoup(self.html.text, "html.parser")
            a_tag = bsObject.select(self.selector[1])
            cnt = 1
            for i in a_tag:
                movie_title = ""
                if ":" in i.attrs['title']:
                    movie_title += str(i.attrs['title']).replace(":", "_")
                else:
                    movie_title += i.attrs['title']
                subUrl = "https://movie.naver.com/movie/{}".format(i.attrs['href'])
                subHtml = req.get(subUrl)
                if subHtml.ok:
                    subBsObject = BeautifulSoup(subHtml.text, "html.parser")
                    img_tag = subBsObject.select_one(self.selector[2])
                    # print (img_tag.attrs['src'])
                    t = urlopen(img_tag.attrs['src']).read()
                    with open(movie_title + "&{}.jpg".format(cnt), 'wb') as f:
                        print (movie_title + ".jpg")
                        f.write(t)
                        f.close()
                    cnt += 1

    def file_search(self):
        for f in os.listdir():
            if self.filtering_one.search(f):
                i_front = self.filtering_one.search(f).span()[1]
                i_rear  = self.filtering_two.search(f).span()[0]
                self.movDict[int(f[i_front:i_rear])] = [os.path.abspath(f), f]

        # 데이터 정렬
        self.movDict = sorted(self.movDict.items(), key=operator.itemgetter(0))
        print (self.movDict)
        tmp = [i[1] for i in self.movDict]
        for k in tmp:
            html = """
                        <html>
                        <head></head>
                        <body>
                         <p><img src='{0}' width=400>{1}</p>
                        </body>
                        </html>
                        """.format(k[0], k[1])
            with open("result.html", "a", encoding='utf-8') as f:
                f.write(html)

        print ("html success !!!")

def main():
    # [+] 작업 디렉토리 이동
    os.chdir("C:/Users/sleep/Desktop/movie")
    mvObject = Movie()
    # mvObject.url_request()
    mvObject.file_search()
if __name__ == "__main__":
    main()