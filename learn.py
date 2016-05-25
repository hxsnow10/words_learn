#encoding=utf-8
import copy
from words import *
from random import random,shuffle
from time import time

def filter0(dic,Max=600):
    rval=[dic[word][0:2] for word in dic if not rem0(dic[word])]
    return rval[:Max]

def filter1(dic,Max=600):
    rval=[dic[word][0:2] for word in dic if not rem1(dic[word])]
    return rval[:Max]

def test(words,dic,path,k):
    MAXB=100
    a=words
    b=[]
    c=[]
    while True:
        if len(a)==0 and len(b)==0:
            break
        if len(b)>MAXB or (len(a)==0 and len(c)==0):
            test_file=open('new_word.txt','w')
            for w in b:
                test_file.write('\t'.join(w)+'\n')
            test_file.close()

            k_words=b[:k]
            b=b[k:]
        else:
            ss=random()
            s=50+len(b)+20+10
            if ss>1-50.0/s:
                k_words=a[:k]
                a=a[k:]
            elif ss>1-(50.0+len(b))/s:
                k_words=b[:k]
                b=b[k:]
            elif ss>1-(50.0+len(b)+20)/s:
                shuffle(c)
                k_words=c[:k]
                c=c[k:]
            else:
                print 'special time'
                k_words=b
                for i in range(len(k_words)):
                    print str(i)+'\t'+'\t'.join(k_words[i])
                ok=raw_input(':\n')
                continue
        if len(k_words)==0:continue
        print '-'*35+'Start'+'-'*35+'\n'
        tt=0
        while len(k_words)>0:
            print '-'*20+'\n'*20
            new_k_words=[]

            for i in range(len(k_words)):
                print k_words[i][0]
                known=raw_input('认识吗 (y/n):\t').strip()
                print '\t'.join([str(j) for j in k_words[i]])
                ok=raw_input(':\t').strip()
                print '\n'
                if known=='n' or ok=='n':
                    if tt==0:
                        dic[k_words[i][0]][2]=dic[k_words[i][0]][2]+1
                        s=dic[k_words[i][0]][6]
                        dic[k_words[i][0]][6]=(s[0]+1,s[1])
                        dic[k_words[i][0]][5]=time()
                        b=b+[k_words[i]]
                    new_k_words=new_k_words+[k_words[i]]
                else:
                    if tt==0:
                        c=c+[k_words[i]]
                        dic[k_words[i][0]][2]=dic[k_words[i][0]][2]/2
                        s=dic[k_words[i][0]][6]
                        dic[k_words[i][0]][6]=(s[0]+1,s[1]+1)
                        dic[k_words[i][0]][5]=time()
            for i in range(len(k_words)):
                print '\t'.join([str(j) for j in k_words[i]])
            ok=raw_input('\n')
            tt=tt+1
            k_words=new_k_words
            if tt==1:kk_words=copy.copy(k_words)
        if len(kk_words)!=0:
            print '\n'*15+'-'*10+'REVIEW:'+'-'*10+'\n'
            for i in range(len(kk_words)):
                print '\t'.join([str(j) for j in kk_words[i]])
            ok=raw_input('\n')
        save(dic,path)
        print '-'*35+'End'+'-'*35
        print len(a),len(b),len(c)

def test_through(words,dic,path,k):#TODO:has bug
    MAXB=100
    a=words
    b=[]
    c=[]
    while True:
        k_words=a[:k]
        a=a[k:]
            
        if len(k_words)==0:continue
        print '-'*35+'Start'+'-'*35+'\n'
        tt=0
        while len(k_words)>0:
            print '-'*20+'\n'*20
            new_k_words=[]

            for i in range(len(k_words)):
                print k_words[i][0]
                known=raw_input('认识吗 (y/n):\t').strip()
                print '\t'.join([str(j) for j in k_words[i]])
                ok=raw_input(':\t').strip()
                print '\n'
                if known=='n' or ok=='n':
                    if tt==0:
                        dic[k_words[i][0]][2]=dic[k_words[i][0]][2]+1
                        s=dic[k_words[i][0]][6]
                        dic[k_words[i][0]][6]=(s[0]+1,s[1])
                        dic[k_words[i][0]][5]=time()
                        b=b+[k_words[i]]
                    new_k_words=new_k_words+[k_words[i]]
                else:
                    if tt==0:
                        c=c+[k_words[i]]
                        dic[k_words[i][0]][2]=dic[k_words[i][0]][2]/2
                        s=dic[k_words[i][0]][6]
                        dic[k_words[i][0]][6]=(s[0]+1,s[1]+1)
                        dic[k_words[i][0]][5]=time()
            for i in range(len(k_words)):
                print '\t'.join([str(j) for j in k_words[i]])
            ok=raw_input('\n')
            tt=tt+1
            k_words=new_k_words
            if tt==1:kk_words=copy.copy(k_words)
        if len(kk_words)!=0:
            print '\n'*15+'-'*10+'REVIEW:'+'-'*10+'\n'
            for i in range(len(kk_words)):
                print '\t'.join([str(j) for j in kk_words[i]])
            ok=raw_input('\n')
        save(dic,path)
        print '-'*35+'End'+'-'*35
        print len(a),len(b),len(c)
            
path='words.txt'
if __name__=='__main__':
    dic=load(path)
    words_to_test=filter0(dic,60000)
    print len(words_to_test)
    fp=open('words_to_learn.txt','w')
    for word,mean in words_to_test:
        fp.write(word+'\t'+mean+'\n')
    fp.close()
    test(words_to_test,dic,path,7)
