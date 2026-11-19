import pandas as pd
import os
import json
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"data","study_log.csv"))
# 1
t=df.pivot_table(index="周几",columns="科目",values="分钟",aggfunc="sum").to_string()
print(t)
# 2
s=pd.to_datetime("2026/" + df["日期"])
v=s.dt.strftime("%Y-%m-%d").tolist()
print(v)
# 3
df2=df.copy()
v1=df2["组内占比"]=(df2["分钟"]/df2.groupby("科目")["分钟"].transform("sum")*100).round(1)
print(df2[["科目","组内占比"]])
# 4
df3=pd.DataFrame({"num":[60,60,60,120,90,80]})
d3=df3.sort_values("num",ascending=False)
d31=d3.rank(method="average",ascending=False)
d32=d3.rank(method="dense",ascending=False)
d33=d3.rank(method="min",ascending=False)
d34=d3.rank(method="first",ascending=False)
print(d31)
print(d32)
print(d33)
print(d34)
# 5
print(df.loc[0:2])
print(df.iloc[0:2])
print(df.loc[df["分钟"]>60,["科目","分钟"]])
print(df.query("分钟>60"))
print(df.query("科目 == 'SQL'"))
# 6
df4=df.copy()
df4["日期"]=pd.to_datetime("2026/"+df4["日期"])
df4=df4.sort_values("日期").reset_index(drop=True)
print(df4["分钟"].cumsum())
print(df4["分钟"].shift(1))
print(df4["分钟"].rolling(3).mean())
# 7
t1=df.head(3).to_dict(orient="records")
t2=json.dumps(t1,ensure_ascii=False)
t3=json.loads(t2)
print(t3)
print(type(t2))
