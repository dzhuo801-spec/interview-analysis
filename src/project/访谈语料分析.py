import pandas as pd
import os
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Microsoft YaHei","SimHei"]
plt.rcParams["axes.unicode_minus"]=False
def load_all(dirpath):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    idt=os.listdir(os.path.join(BASE,dirpath))
    d=[]
    for i in idt:
        if i.startswith("interviews"):
            df=pd.read_csv(os.path.join(BASE,dirpath,i))
            d.append(df)
    return pd.concat(d,ignore_index=True)
df=load_all("data")
def clean(df):
    print(df.shape)
    print(df.isnull().sum())
    d=df["text"].str.strip()
    print((d.str.len()==0).sum())
    print(df.duplicated(subset=["id","speaker","text"]).sum())
    print(df.duplicated(subset=["text"]).sum())
    print(len(df.drop_duplicates(subset=["text"])))
    print(f"{df["id"].min()}到{df["id"].max()}")
    print(len(df.drop_duplicates(subset="id")))
    return df
#     # df1=df.drop_duplicates()
#     # print(df1.isnull().sum())
#     # print(pd.to_datetime("2026/" + df["日期"]).dt.year.value_counts().to_dict())
df=clean(df)
df["字数"]=df["text"].str.strip().str.len()
zi=df.groupby("speaker")["字数"].agg(["count","sum","mean"])
zi1=zi.sort_values("speaker",ascending=True).round(1)
zi1["占比"]=(df.groupby("speaker")["字数"].count()/len(df)*100).round(1)
zi1=zi1.reset_index()
print(zi1)
zi2=df["text"].value_counts().sort_values(ascending=False).head(10).reset_index()
zi3=df.groupby("text")["speaker"].agg(["count","nunique"]).sort_values(["count","nunique"],ascending=False)
zi3=zi3.rename(columns={"count":"次数","nunique":"人数"}).reset_index()
zi4=zi3.head(10)
print(zi2)
print(zi4)
# df["条数占比"]=(df["speaker"].count().transform("sum")/len(df)).round(1)
# print(df.groupby("speaker")["条数占比"].sum())
# def report(df,group_col,value_col):
#     return df.groupby(group_col)[value_col].agg(["sum","mean","count"]).sort_values(["sum","mean","count"],ascending=False).round(2)
# print(report(df,"科目","分钟"))
def save(df,outpath):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    df.to_csv(os.path.join(BASE,outpath,"output.csv"),index=False, encoding="utf-8-sig")
    df.to_excel(os.path.join(BASE,outpath,"output.xlsx"),index=False)
save(df,"output/")
def poive(labels,values,path):
    fig,ax=plt.subplots(figsize=(8,4))
    ax.barh(labels,values,color="#F5A623")
    ax.set_title("图表")
    ax.set_xlabel("条数")
    for i,v in enumerate(values):
        ax.text(v+0.1,i,str(v),va="center")
    fig.tight_layout()
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ipx=os.path.join(BASE,"output",path)
    fig.savefig(ipx,dpi=100)
    plt.close(fig)
    print(f"图已生成:{ipx}")
poive(zi1["speaker"],zi1["count"],"访谈_说话人.png")
poive(zi2["text"],zi2["count"],"访谈_话题.png")
def csv_clean(x,path):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ipx=os.path.join(BASE,"output",path)
    x.to_csv(ipx,index=False,encoding="utf-8-sig")
    print(f"csv已生成:{ipx}")
csv_clean(zi1,"访谈_说话人.csv")
csv_clean(zi3,"访谈_话题.csv")
def excel_clean(x,y,path):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ipx=os.path.join(BASE,"output",path)
    with pd.ExcelWriter(ipx) as writer:
        x.to_excel(writer, sheet_name="说话人",index=False)
        y.to_excel(writer,sheet_name="话题",index=False)
        print(f"excel已生成:{ipx}")
excel_clean(zi1,zi3,"访谈_分析.xlsx")