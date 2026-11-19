import os
import pandas as pd
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"output","访谈标签表.csv"),encoding="utf-8-sig")
mp=pd.read_csv(os.path.join(BASE,"output","主题归并表.csv"),encoding="utf-8-sig")
mapping=dict(zip(mp["原主题"],mp["归并后"]))
df["主题归并"]=df["主题"].map(mapping)
print(df["主题归并"].nunique())
print(df["主题归并"].isnull().sum())
print(df["主题归并"].count())
print(df.groupby("主题归并")["id"].count())
df.to_csv(os.path.join(BASE,"output","访谈标签表_归并.csv"), index=False, encoding="utf-8-sig")