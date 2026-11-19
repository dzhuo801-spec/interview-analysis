import pandas as pd
import os
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Microsoft YaHei","SimHei"]
plt.rcParams["axes.unicode_minus"]=False
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"data","study_log.csv"))
print(df.shape)
print(df.columns.tolist())
print(df.isna().sum())
print(df.duplicated().sum())
print(len(df.drop_duplicates(subset=["内容"])))
zi1=df.groupby("科目")["分钟"].agg(["count","sum","mean"]).round(1).sort_values(["count","sum","mean"],ascending=False)
zi1["占比%"]=(df.groupby("科目")["分钟"].sum()/df["分钟"].sum()*100).round(1)
zi1=zi1.rename(columns={"count":"条数","sum":"总分钟","mean":"平均"}).reset_index()
print(zi1)
week=["周一","周二","周三","周四","周五","周六","周日"]
zi2=df.groupby("周几")["分钟"].agg(["count","sum","mean"]).round(1).reindex(week).reset_index()
zi2=zi2.rename(columns={"count":"条数","sum":"总分钟","mean":"平均"})
print(zi2)
df["日期"]=pd.to_datetime("2026/"+df["日期"])
s=len(df.drop_duplicates(subset=["日期"]))
print("唯一日期：",s)
print(df)
print("范围：",f"{df["日期"].min()}~{df["日期"].max()}")
days=df.groupby("日期")["分钟"].sum()
print("每天合计：",days)
print("累计：",days.cumsum().iloc[-1])
def povile(labels,value,path):
    fig,ax=plt.subplots(figsize=(8,4))
    ax.barh(labels,value,color="#F5A623")
    ax.set_title("学习表")
    ax.set_xlabel("条数")
    for i,v in enumerate(value):
        ax.text(v+0.1,i,str(v),va="center")
    fig.tight_layout()
    ipx=os.path.join(BASE,"output",path)
    fig.savefig(ipx,dpi=100)
    plt.close()
    print(f"图片已生成:{ipx}")
povile(zi1["科目"],zi1["条数"],"科目_个数")
povile(zi2["周几"],zi2["条数"],"周几_个数")
def csv_clean(x,path):
    ipx=os.path.join(BASE,"output",path)
    x.to_csv(ipx,index=False,encoding="utf-8-sig")
    print(f"csv已生成:{ipx}")
csv_clean(zi1,"学习统计_科目.csv")
csv_clean(zi2,"学习统计_周几.csv")
def excel_clean(x,y,path):
    ipx=os.path.join(BASE,"output",path)
    with pd.ExcelWriter(ipx) as writer:
        x.to_excel(writer,sheet_name="科目",index=False)
        y.to_excel(writer,sheet_name="周几",index=False)
    print(f"excel已生成:{ipx}")
excel_clean(zi1,zi2,"学习时间分析.xlsx")