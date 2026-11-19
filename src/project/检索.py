# 我的猜测（先猜后验）
# 手艺            → 6条
# 婚俗变迁        → 11 条
# 手艺 + 传统手艺 → 6 条
# 祭祖            →0 条
import os.path
import pandas as pd
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df=pd.read_csv(os.path.join(BASE,"output","访谈标签表_归并.csv"),encoding="utf-8-sig")
def retrieve(关键词=None,主题=None,大类=None):
    cond=pd.Series(True,index=df.index)
    if 关键词:
        cond=cond & df["text"].str.contains(关键词,na=False)
    if 主题:
        cond=cond & (df["主题"] == 主题)
    if 大类:
        cond=cond & (df["主题归并"] == 大类)
    hits = df[cond]
    print(f"命中 {len(hits)} 条 ｜ 关键词={关键词 or '（不限）'} ｜ 主题={主题 or '（不限）'} ｜ 大类={大类 or '（不限）'}")
    v1=hits["主题"].value_counts()
    if len(v1)>0:
        total=len(v1)
        total_in=" / ".join([f"{i}{v}" for i,v in v1.items()])
        print(f"来自 {total} 个原主题：{total_in}")
    if len(hits) == 0:
        print("（一条都没有）")
    else:
        for _, row in hits.head(3).iterrows():
            print(f"【{row['id']} · {row['speaker']}】{row['text']}")
    return hits
retrieve("手艺")
retrieve("婚俗","婚俗变迁")
retrieve(主题="婚俗变迁")
retrieve("手艺", "传统手艺")
retrieve("祭祖")
retrieve("手艺", "婚俗变迁")
retrieve(大类="生计与流动")
retrieve(大类="礼俗与规矩")
retrieve(大类="生计与流动", 主题="变化")
retrieve(主题="变化")
retrieve(大类="不存在")