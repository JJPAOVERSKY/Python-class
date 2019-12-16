from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#-------------------------
#1.构建url
url="http://www.wtu.edu.cn/"
#2.构建request
#访问主页的结果存放在r中
r = request.urlopen(url)
#3.查看请求结果
print(type(r))
print(r.getcode())
print(r)
page_content = r.read()
print(page_content.decode('utf-8'))
#4.打开网页存放到本地
with open('./all.html', 'wb')as fp:
    fp.write(page_content)