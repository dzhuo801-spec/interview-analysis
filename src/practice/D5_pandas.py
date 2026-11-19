import pandas as pd
import os
import csv
# 1
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"data","study_log.csv"))
print("shape=",df.shape)
print("列名=",df.columns.tolist())
print("前五行：",df.head(5))
print("分钟：",df.describe())
# 2 少写了括号会报错
print("科目",df["科目"][:5])
print(df[["科目","分钟"]][:3])
# 3
print(df[df["分钟"]>70][["日期","科目","分钟"]])
# 4
print(df.sort_values("分钟",ascending=False)[["日期","科目","分钟"]][:5])
print(df[df["科目"] =="休息"][["日期","科目","分钟"]])
print(df[df["分钟"] > 0][["日期","科目","分钟"]])
# 5
print(df.groupby("科目").size().sort_values(ascending=False))
# 6
print(df.groupby("科目")["分钟"].sum().sort_values(ascending=False))
# 7
print(df.groupby("科目")["分钟"].agg(["sum","mean","count"]).round(1))
# 8
pct = df.groupby("科目")["分钟"].sum() / df["分钟"].sum() * 100
print(pct.round(1))
# 9
df["小时"]=(df["分钟"]/60).round(1)
print(df[["日期","科目","分钟","小时"]])
print(df.groupby("周几")["分钟"].sum()[:3])
# 10
r=df.groupby("科目")["分钟"].sum()
r2=r.reset_index()
print(r2)
print(r2.columns.tolist())
r3 = r2.rename(columns={"分钟": "总分钟"})
print(r3.columns.tolist())
r3.to_csv(os.path.join(BASE,"output","study_by_pandas.csv"), index=False, encoding='utf-8-sig')
back = pd.read_csv(os.path.join(BASE,"output","study_by_pandas.csv"))
print(back.shape)
print(back.columns.tolist())
# 11
a=pd.read_csv(os.path.join(BASE,"data","interviews.csv"))
b=pd.read_csv(os.path.join(BASE,"data","interviews_batch2.csv"))
back2=pd.concat([a,b],ignore_index=True)
print(back2.shape)
print(back2["speaker"].unique())
print(back2.groupby("speaker").size())
# 12
back2["字数"]=back2["text"].str.len()
print(back2.sort_values("字数",ascending=False)[["id","speaker","字数"]][:5])
print((back2["字数"] == 17).sum())
# 最多的是7行
print(df["内容"].str.contains("练习"))
print(df[df["内容"].str.contains("练习")]["科目"].unique())
print((df["内容"].str.contains("练习") == True).sum())
# 都是sql
# 13 附
import sqlite3,pandas as pd
conn=sqlite3.connect(r"E:\ai\interview-analysis\sql\practice.db")
emp=pd.read_sql("SELECT * FROM employees",conn)
der=pd.read_sql("SELECT * FROM departments",conn)
print(emp.shape)
print(emp.head())
print(der.shape)
print(der.head())
# 13
salary_avg=emp.groupby("dept_id",as_index=False)["salary"].mean().rename(columns=({"salary":"部门均薪"}))
m=emp.merge(salary_avg,on="dept_id",how="left").round(2)
x1=m[m["salary"]>m["部门均薪"]]
d=der.rename(columns=({"id":"dept_id","name":"部门"}))
mx=x1.merge(d,on="dept_id",how="left")
v1=mx[["name","部门","salary","部门均薪"]]
print(v1.to_string(index=False))
# 14
a=emp[emp["salary"]>=25000]
b=emp[emp["manager_id"].isnull()]
s=pd.concat([a,b],ignore_index=True)
s1=s.drop_duplicates()[["name","salary"]]
print(s1.shape)
# 附录
print(emp["manager_id"].isnull().sum())
print(emp.dropna(subset=["manager_id"]).shape)
print(emp["manager_id"].fillna(0).shape)
print(df["科目"].value_counts())













conn.close()






