#encoding=utf-8
from ask import *
from fanyi import *
def all_en(x):
    for i in x:
        if not (i>='a' and i<='z'):
            return False
    return True

path='words.txt'
if __name__=='__main__':
    dic=load(path)
    for w in dic:
        mean=dic[w][1]
        if all_en(mean):
            new_m=query(w)
            if new_m!=w:
                dic[w][1]=new_m
                print 'update',w,new_m
            else:
                del dic[w]
                print 'del',w
    save(dic,path)
