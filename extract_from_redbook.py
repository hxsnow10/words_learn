#encoding=utf-8
from ask import *

if __name__=='__main__':
    path='words.txt'
    dic=load(path)
    fp=open('GRE红宝书.txt','r')
    s=0
    for l in fp:
        line=l.decode('gbk').encode('utf-8')
        if line.strip()=='':
            s=(s+1)%3
        else:
            if s==0:
                word=line.strip()
            elif s==1:
                mean=line.strip()
                tt=time()
                item=[word,mean,'1',tt,tt,(1,0)]
                add(dic,item)
            else:
                pass
                
    save(dic,path)
        
