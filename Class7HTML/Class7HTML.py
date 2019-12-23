from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#-------------------------
#1.构建url
# url="https://baijiahao.baidu.com/s?id=1623548638746241393&wfr=spider&for=pc"
#2.构建request
#访问主页的结果存放在r中
# r = request.urlopen(url)
#3.查看请求结果
# print(type(r))
# print(r.getcode())
# print(r)
# page_content = r.read()
# print(page_content.decode('utf-8'))
#4.打开网页存放到本地
# with open('./top.html', 'wb')as fp:
#     fp.write(page_content)

# ===============================================================

# path = './top.html'
from bs4 import BeautifulSoup
# with open(path, encoding='utf-8') as data:
#     soup = BeautifulSoup(data,"html.parser")
# 1.查看页面的 Title
#print(soup.title)
# 2.查看页面的 p 标签
# print(soup .p)
# print(soup .p.contents)
# print(soup .p.string)
# print(soup .p['calss'])
# print(soup .p['class'][0])
# print(soup .p.b)

# ==============================

# 3.查找批量对象/标签

# s1 = soup.find('p')
# print(s1)

# s2 = soup.find_all('p')
# print(s2)

# ===============================================================================
import urllib
url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
r = urllib.requet.urlopen(url)
s = r.read()
soup = BeautifulSoup(s , 'html.parser')

data = soup.find_all('tr')

for tr in data:
    ltd = tr.find_all('tr')
    allUni = []
    sngUni = []
    for td in ltd:
        sngUni.append(td.string)
    allUni.append(sngUni)
print(allUni[0])
print(allUni[1])
print(allUni[2])

with open('./_uni_ph.csv','w') as fp: