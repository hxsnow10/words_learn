#encoding=utf-8
from words import *
from time import time,ctime

path='words.txt'
query=iciba_word_mean
if __name__=='__main__':
    dic=load(path)
    n=0
    while True:
        n=n+1
        s=[7,49,49*2,49*3,49*4,49*5,49*6,49*7]
        for k in s:
            if n%k==0:
                print '\nReview'
                for w in dic.values()[-k:]:
                    print '\t'.join(w[0:2])
                s=raw_input('')
        try:
            word=raw_input('Enter word to ask:').strip()
            print word
            item=ask(dic,word)
            if item==None:
                print("Can't find it")
                s=query(word)
                print('meaning of '+word+':'+s)
                tt=time()
                item=[word,s,0,tt,0,tt,(1,0),str([])]
            print '\t'.join([str(i) for i in item[0:3]])
            item[2]=item[2]+1
            item[5]=time()
            add(dic,item)
        except Exception, e:
            print e
        save(dic,path)
