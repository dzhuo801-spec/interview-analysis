import pandas as pd
import os
def load_all(dirpath):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    id=os.listdir(os.path.join(BASE,dirpath))
    d=[]
    for i in id:
        df=pd.read_csv(os.path.join(BASE,dirpath,i))
        d.append(df)
    return pd.concat(d,ignore_index=True)
df=load_all("data")
def cleam(df):
    df1=df.drop_duplicates()
    print(df1.isnull().sum())
    print(pd.to_datetime("2026/" + df["日期"]).dt.year.value_counts().to_dict())
cleam(df)
def report(df,group_col,value_col):
    return df.groupby(group_col)[value_col].agg(["sum","mean","count"]).sort_values(["sum","mean","count"],ascending=False).round(2)
print(report(df,"科目","分钟"))
def save(df,outpath):
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    df.to_csv(os.path.join(BASE,outpath,"output.csv"),index=False, encoding="utf-8-sig")
    df.to_excel(os.path.join(BASE,outpath,"output.xlsx"),index=False)
save(df,"output/")