# 爬取杉本有美吧所有杉本有美的图片
import re
import requests
import urllib
from fake_useragent import UserAgent

ua = UserAgent()

url='https://tieba.baidu.com/p/2166231880?red_tag=0132652500'

headers={
    'Host': 'tieba.baidu.com',
    "User-Agent": ua.random
}

res=requests.get(url=url,headers=headers)

def resMatch(data):
    reg=r'class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/\w+=\S+"'
    for i in re.findall(reg,data):
        reg1=r'https://imgsa.baidu.com/forum/w%3D580/\w+=\S+.jpg'
        res=re.findall(reg1,i)[0]
        urllib.request.urlretrieve(res,'F:/'+res.split('/')[6])

print(resMatch(res.text))