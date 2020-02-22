#-*- coding:utf-8 -*-
from gensim.summarization.summarizer import summarize
f = open("result1.txt", 'rt', encoding='utf-8-sig')
All=f.read()
f.close()
lines=All.split('\n')
strs = ''
for line in lines:
    if line is not '':
        strs = strs + line
a = summarize(strs, ratio=0.1)
f1 = open('result2.txt', 'w', encoding='utf-8-sig')
f1.write(a)
f1.close()