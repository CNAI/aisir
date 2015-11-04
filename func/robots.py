__author__ = 'r'
#coding=utf-8
from urllib import request,parse
import json
def getdata(info):
    info = parse.quote(info)
    url = 'http://www.tuling123.com/openapi/api?key=58750b84ad4a81d69ba48857ffc2be1d&info='+info
    res = request.urlopen(url).read().decode()
    res= json.loads(res)
    if(res['code']==100000):
       return res['text']
    else:
        return '不知道您在说什么'

