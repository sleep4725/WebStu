import requests as req
from bs4 import BeautifulSoup
import pprint as ppr
import re
from urllib.request import (urlretrieve, urlopen)
import os
#___________________________________________________________
class Scarpping:
    def __init__(self):
        self.url = "https://pixabay.com/ko/photos/?"
        self.params = {
            'q':'%EA%B7%80%EC%97%AC%EC%9A%B4+%EA%B3%A0%EC%96%91%EC%9D%B4',
            'image_type':'all',
            'pagi':None
        }
        self.re = re.compile('jpg$')

    def url_request(self):
        for p_ in range(1, 56):
            self.params['pagi'] = p_
            html = req.get(self.url, self.params)
            if html.status_code == 200:
                bs_object = BeautifulSoup(html.text, "html.parser")
                img_data = bs_object.select('#content > div > div > div > div.flex_grid.credits > div > a > img')

                print("{}_page ++++++++++++++++++++++++++++++++++++++++++".format(p_))
                cnt = 1
                for x in ([i.attrs for i in img_data]):
                    for j in x.values():
                        if self.re.search(j):
                            print ("{}번째 데이터 {} 처리 중 ...".format(cnt, j))
                            name = "cat_{page}_{cnt}.jpg".format(page = p_,cnt = cnt)
                            t = urlopen(j).read()
                            with open(name, 'wb') as f:
                                f.write(t)
                                f.close()
                            cnt += 1
def main():
    os.chdir('C:/Users/sleep/Desktop/Image')
    obj = Scarpping()
    obj.url_request()

if __name__ == "__main__":
    main()