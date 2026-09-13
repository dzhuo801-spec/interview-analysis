"""生成第二批访谈语料（第二批田野调查）

为什么要第二个文件？
→ 周四的练习是「一次读取多个访谈文件」，一个文件测不出来。
→ 顺便模拟真实场景：你的田野调查通常分好几批做，文件也是好几个。

运行：.venv\\Scripts\\python.exe src\\make_fake_data2.py
      （这个脚本只用标准库，用 `py` 也能跑；但项目里统一用 venv，省得记）

[!] 注意：这个脚本是【一次性】的。
    每跑一次都会随机重新生成 data/interviews_batch2.csv，覆盖旧数据。
    只在【确实想换一批数据】时才跑它。
"""
import csv
import os
import random

SPEAKERS = ["访谈者", "受访者D", "受访者E", "受访者F"]

SENTENCES = [
    "现在年轻人都不愿意留在村里了",
    "我们村的祠堂前年刚修过",
    "以前结婚要摆三天酒现在一天就完了",
    "老人走了以后这些东西就没人记得了",
    "外面打工一年能挣不少钱",
    "孩子上学要去县城住校",
    "村里现在就剩老人和小孩",
    "这个节日以前很热闹的",
    "年轻人不懂这些规矩了",
    "现在谁还种地啊都是买着吃",
    "我们这边讲究的是礼数",
    "家里老人身体还行",
]

rows = []
for i in range(40):
    speaker = random.choice(SPEAKERS)
    text = random.choice(SENTENCES)
    rows.append([i + 101, speaker, text])       # id 从 101 开始，和第一批区分开

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(base, "data", "interviews_batch2.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)

with open(out, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "speaker", "text"])
    writer.writerows(rows)

print(f"已生成 {out}，共 {len(rows)} 条（说话人：{', '.join(SPEAKERS)}）")
