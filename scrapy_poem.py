#-*-coding:utf-8-*-
import json
import sys
import hashlib
import requests

# http://api.apiopen.top/likePoetry?name=%E9%87%8D%E9%98%B3%E8%8A%82
# https://v2.jinrishici.com/info
# https://v2.jinrishici.com/one.json

# r = requests.get('https://api.github.com/events')

from hashlib import md5
import random

appid = '20180801000190815' #你的appid
secretKey = 'g4dmvSLSFVCOwMZzsqaD' #你的密钥

 
httpClient = None
myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
q = '您好'
fromLang = 'zh'
toLang = 'en'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
# print(type(myurl))
try:
    req = requests.get(myurl)
    print(req.content)
except Exception as e:
    print(e)
