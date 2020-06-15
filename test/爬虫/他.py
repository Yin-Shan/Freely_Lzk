import urllib.request
import chardet
import requests

u = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#page = urllib.request.urlopen(u) #打开网页
#htmlCode = page.read() #获取网页源代码

#print(chardet.detect(htmlCode)) #打印返回网页的编码方式
#print('------------')
#print(htmlCode.decode('utf-8')) #打印网页源代码
strhtml = requests.get(u)        #Get方式获取网页数据
print(strhtml.text)