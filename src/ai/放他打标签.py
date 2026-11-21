import pandas as pd
import os
import json
import requests
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Microsoft YaHei","SimHei"]
plt.rcParams["axes.unicode_minus"]=False
KEY = open(os.path.join(os.path.dirname(__file__), "key.txt"), encoding="utf-8").read().strip()
用量=[]
def text_tab(文本):
    r = requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={"Authorization": f"Bearer {KEY}"},
    json={
         "model": "deepseek-flash",
            "temperature": 0,
            "thinking": {"type": "disabled"},
        # 放弃思考
            "messages": [
                {"role": "system", "content": '只输出一个 json，不要解释、不要代码块，提及人物，提及的是谁：比如说老一辈，年轻人，小孩。并且主题禁止使用[变迁/变化/其他]万金油的词，主题必须是具体是事务，不是抽象的过程'
                                              '格式：{"主题": "一个词", "情绪": "一个词","人物": "一个词"}'},
                {"role": "user", "content": 文本},
            ],
        },
    )
    print(r.status_code)
    print(r.json()["usage"])
    用量.append(r.json()["usage"])
    return r.json()["choices"][0]["message"]["content"]
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
idt=os.listdir(os.path.join(BASE,"data"))
d=[]
for i in idt:
    if i.startswith("interviews"):
            df=pd.read_csv(os.path.join(BASE,"data",i))
            d.append(df)
df=pd.concat(d,ignore_index=True)
结果=[]
失败=[]
n=0
for i, 说话人, 内容 in zip(df["id"], df["speaker"], df["text"]):
    n=n+1
    print(n,end="",flush=True)
    try:
        num = json.loads(text_tab(内容))
        hear1 = {"id": i, "speaker": 说话人, "text": 内容, **num}
        结果.append(hear1)
    except Exception as e:
        失败.append({"id":i,"text":内容,"错误":str(e)})
print()
print("成功",len(结果),"失败",len(失败))
df2 = pd.DataFrame(结果)
print(df2.shape)
df2.to_csv(os.path.join(BASE, "output", "访谈标签表_B.csv"), index=False, encoding="utf-8-sig")
print(df2)
print(df2["主题"].value_counts())
print(df2["情绪"].value_counts())
print(df2["人物"].value_counts())
zi=df2["主题"].value_counts().sort_values(ascending=True)
zi1=df2["人物"].value_counts().sort_values(ascending=True)
def plot(labels,values,path):
    fig,ax=plt.subplots(figsize=(9,8))
    ax.barh(labels,values,color="#0000FF")
    ax.set_title(f"访谈语料分布({len(df2)}条/{len(labels)}种)")
    ax.set_xlabel("次数")
    for i,v in enumerate(values):
        ax.text(v+0.1,i,str(v),va="center")
    fig.tight_layout()
    BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ipx=os.path.join(BASE,"output",path)
    fig.savefig(ipx,dpi=100)
    plt.close()
    print(f"图已经生成:{ipx}")
plot(zi.index,zi.values,"访谈_主题分布.png")
plot(zi1.index,zi1.values,"访谈_人物.png")
def csv_cla(path):
    return df2.to_csv(os.path.join(os.path.dirname(__file__),path),index=False,encoding="utf-8-sig")
csv_cla("table.csv")
总p=0
总c=0
for u in 用量:
    总p=总p+u["prompt_tokens"]
    总c=总c+u["completion_tokens"]
ts=总p/1000000*1+总c/1000000*4
print("调用次数",len(用量))
print("总prompt",总p)
print("总completion",总c)
print("单条平均prompt",总p/len(用量))
print("总成本（元）",ts)
总hit=0
总miss=0
for u in 用量:
    总hit=总hit+u["prompt_cache_hit_tokens"]
    总miss=总miss+u["prompt_cache_miss_tokens"]
print("命中",总hit)
print("未命中",总miss)