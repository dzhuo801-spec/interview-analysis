"""make_fake_data.py —— 生成假的访谈语料，用来练手

惯例：先用假数据把流程跑通，再换成真数据。
好处：把「技术问题」和「数据问题」分开解决，不然两种问题混在一起很难排错。

运行：py src/make_fake_data.py
"""
import csv
import os
import random

# 假的说话人（对应你田野调查里的访谈对象）
SPEAKERS = ["访谈者", "受访者A", "受访者B", "受访者C"]

# 假的语料（模仿访谈里会出现的话）
SENTENCES = [
    "我们这边的婚俗这几年变化挺大的",
    "老一辈还是很看重这个仪式",
    "年轻人出去打工以后回来就不太一样了",
    "过节的时候全村都会回来",
    "现在办酒席的钱比以前多很多",
    "村里的老人越来越少见了",
    "这个手艺现在没几个人会了",
    "小孩都在镇上读书",
    "以前都是走路去赶集现在有车了",
    "家里种的菜够自己吃",
]

# ---------- 造数据 ----------
rows = []                                    # 空列表，用来装所有行
for i in range(50):                          # 循环 50 次，造 50 条记录
    speaker = random.choice(SPEAKERS)        # 从列表里随机挑一个
    text = random.choice(SENTENCES)
    rows.append([i + 1, speaker, text])      # 三个值组成一行，塞进列表

# ---------- 写出文件 ----------
# 相对路径：基于项目根目录，别人 clone 下来也能跑
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(base, "data", "interviews.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)

# encoding="utf-8-sig" 是为了让 Excel 打开不乱码（用 utf-8 会乱码，这个坑你早晚会踩）
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "speaker", "text"])   # 先写表头
    writer.writerows(rows)                       # 再写所有数据行

print(f"已生成 {out}，共 {len(rows)} 条")
