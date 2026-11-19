import os
import pandas as pd
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"output","访谈标签表.csv"),encoding="utf-8-sig")
def retrieve2(人物=None,情绪=None):
    conm=pd.Series(True,index=df.index)
    if 人物:
        conm = conm & (df["人物"] == 人物)
    if 情绪:
        conm = conm & (df["情绪"] == 情绪)
    lft=df[conm]
    print(f"命中 {len(lft)} 条 ｜ 人物={人物 or '（不限）'} ｜ 情绪={情绪 or '（不限）'}")
    if len(lft) == 0:
        print("（什么都没有哦）")
    else:
        for _, row in lft.head(3).iterrows():
            print(f"【{row['id']} · {row['speaker']}】{row['text']}")
    return lft
retrieve2(人物="年轻人")
retrieve2(情绪="感慨")
retrieve2(人物="老一辈", 情绪="感慨")
retrieve2()
retrieve2(人物="访谈者")