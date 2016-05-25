#encoding=utf-8
from collections import OrderedDict
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from ask import *
strong_mode=True

fp=open('3000.txt','r')
text=fp.readlines()
words=OrderedDict()
#each word is a dict of keys=[spell, pronoun, items]
#each item is a dict of keys=[spell, meaning, example, similar, antonym]


def get_spell(line):
    return line.split(' ')[0]
def get_meaning(line):
    return line.split('】')[-1]
def get_example(line):
    return line.split('】')[-1]
def get_similar(line):
    return [w.strip() for w in line.split('】')[-1].split(',')]
def get_antoym(line):
    line=''.join(line.split(' ')[:-1])
    return [w.strip() for w in line.split('】')[-1].split(',')]

spell=None
k=0
while k<len(text):
    line=text[k].strip()
    if len(line)==0:
        k=k+1
        continue
    #print line,
    try:
        line=line.decode('gbk').encode('utf-8') 
    except:
        print k,line
        k=k+1
        continue   
    if line[-1]==']' or line[-2:]=='].':
        #print 'matched 1'
        spell=get_spell(line)
        word={'spell':spell, 'pronoun':'', 'items':[]}
        words[spell]=word
    elif len(line)<9:
        pass
    elif line[0:9]=='【考法':
        #print 'matched 2'
        meaning=get_meaning(line)
        item={'spell':spell, 'meaning':meaning, 'example':'', 'similar':[], 'antonym':[]}
        word['items'].append(item)
    elif line[0:9]=='【例】':
        #print 'matched 3'
        item['example']=get_example(line)
    elif line[0:9]=='【近】':
        #print 'matched 4'
        item['similar']=get_similar(line)
    elif line[0:9]=='【反】':
        #print 'matched 5'
        item['antonym']=get_antoym(line)
    else:
        pass
        #print 'not matched'
    k=k+1
wordss=set([words[w]['spell'] for w in words])

def get_cn(x):
    return x.split('.')[-1].split('：')[0]

def get_m(word):
    mean=[]
    for item in word['items']:
        mean=mean+[get_cn(item['meaning'])]
    mean=';'.join(mean)
    return mean

path='new_words.txt'
if __name__=='__main__':
    dic=OrderedDict([])
    n=0
    ss=[(word,get_m(words[word])) for word in words]
    ss=sorted(ss,key=lambda item:item[0][::-1])
    for word,mean in ss:
        tt=time()
        dic[word]=[word,mean,1,tt,tt]
                
    save(dic,path)
