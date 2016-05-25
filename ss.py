#encoding=utf-8
from words import *

path='words_iciba.txt'
fp=open('wrong_words.txt','r')
words_list=[line.strip() for line in fp]
fp.close()
fp=open('wrong_words.txt','w')
if __name__=='__main__':
    dic=load(path)
    for w in words_list:
        print w
        try:
            mean=iciba_word_mean(w)
            print mean
            dic[w][1]=mean
        except:
            fp.write(w+'\n')
    save(dic,path)
