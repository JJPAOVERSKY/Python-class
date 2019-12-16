import urllib
from bs4 import BeautifulSoup
path = './new.html'
with open(path, encoding='utf-8') as data:
    soup = BeautifulSoup(data,"html.parser")
# 1.查看页面的 Title
#print(soup.title)
# 2.查看页面的 p 标签
print(soup .p)
print(soup .p.contents)
print(soup .p.string)
print(soup .p['calss'])
print(soup .p['class'][0])
print(soup .p.b)