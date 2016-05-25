#encoding=utf-8
import readline
from collections import OrderedDict
import httplib
import md5
import urllib
import random
import json
import urllib2

#about word dic
def load(path):
    wd=open(path,'r')
    dic=OrderedDict()
    for line in wd:
        item=line.strip().split('\t')
        item[2:]=[eval(i) for i in item[2:]]
        dic[item[0]]=item
    wd.close()
    return dic

def save(dic,path):
    wd=open(path,'w')
    for word in dic:
        wd.write('\t'.join([str(i) for i in dic[word]])+'\n')
    wd.close()

def ask(dic,word):
    if word in dic:
        return dic[word]
    else:return None

def add(dic,word_item):
    dic[word_item[0]]=word_item

#about word_item
def rem0(item):
    a=item[6]
    return item[2]<1

def rem1(item):
    a=item[6]
    return (a[1]*1.0+0.01)/(a[0]+0.01)>0.7 and item[2]<1 #and true_time>false_time

def baidu_word_mean(word):
    appid = '20160124000009293'
    secretKey = 'JjqiwfwxmHoDtkEGYpEh'
    httpClient = None
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    sign = appid+word+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = '/api/trans/vip/translate'
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    httpClient.request('GET', myurl)
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    a=eval(response.read())["trans_result"][0]['dst']
    a=eval("u'"+a+"'")
    return  a.encode('utf-8')

def iciba_word_mean(word):
    url='http://dict-co.iciba.com/api/dictionary.php?key=A7169D08C1A1BD26FFDFA31D22BD2109&type=json&w='+word
    dd=json.loads(urllib2.urlopen(url, timeout=5).read())
    mean=';'.join([ p[u'part'].encode('utf-8')+','.join(p[u'means']).encode('utf-8') for p in dd[u'symbols'][0][u'parts']])
    return mean
    
