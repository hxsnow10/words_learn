#encoding=utf-8
from ask import *
import time
path='words.txt'
query=ciabi_word_mean

def analysis(kindel_path):
    fp=open(kindel_path,'r').readlines()
    rval=[]
    ll=0
    word=None
    i=0
    while i<len(fp):
        line=fp[i]
        if line.strip()=='':
            i=i+1
            ll=0
        else:
            if ll==0:
                word=line.split('(')[-1].split(')')[0]
                ll=1
            else:
                s=line.replace('《','\t').replace('》','\t')
                s=[j.strip() for j in s.split('\t')]
                s[-1]=time.mktime(time.strptime(s[-1],'%Y-%m-%d %H:%M:%S'))
                rval.append([word]+s)
                if len([word]+s)!=4:
                    print word,s,line,i
        i=i+1
    return rval
    

if __name__=='__main__':
    dic=load(path)
    kindel_path='kindle_words.txt'
    
    for word,sent,source,tt in analysis(kindel_path):
        print '\n'*20+'-'*20
        print 'word:\t',word
        print 'sent:\t',sent
        print ''
        if word in dic:
            s=dic[word][1]
            item=dic[word]
            print '\t'.join([str(i) for i in item[0:3]])
            item[2]=item[2]+1
            item[5]=tt
            if sent not in eval(dic[word][6]):
                item[6]=str(eval(dic[word][6])+[(sent,source,'')])
            add(dic,item)
        else:
            s=query(word)
            print 'translate'
            item=[word,s,0,tt,0,tt,(1,0),[(sent,source,'')]]
            print '\t'.join([str(i) for i in item[0:3]])
            item[2]=item[2]+1
            add(dic,item)
        save(dic,path)
