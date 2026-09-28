import jieba
import logging
import os
import csv
from collections import Counter
jieba.setLogLevel(logging.WARNING)
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(BASE,"data","interviews.csv"),"r",encoding="utf-8-sig") as f:
    words=[]
    for row in csv.DictReader(f):
        words+=jieba.lcut(row["text"])
        word_count=Counter(words)
def save_counter(counter, path):
    with open(os.path.join(BASE,path),"w",encoding="utf-8-sig",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["词","次数"])
        for word,count in word_count.most_common():
                writer.writerow([word,count])
save_counter(word_count,"output/word_freq.csv")