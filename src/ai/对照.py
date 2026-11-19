import pandas as pd
import os
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
t=pd.read_csv(os.path.join(BASE,"output","访谈_话题.csv"))
lab=pd.read_csv(os.path.join(BASE,"output","访谈标签表_B.csv"))
s=lab.groupby("text")["主题"].agg(lambda s:"/".join(set(s)))
out=t.merge(s,on="text",how="left").reset_index()
print(out)