# -*- coding: utf-8 -*-
r"""题 8 重写专用（2026-10-05）

════════════════════════════════════════════════════════════
  ⭐ 规则（就一条）：
     不许回头看 tests\周日整合卷.py 里已经写好的那一份。
     凭你现在的理解（"os.listdir 是列出目录里的名字"），从空函数写出来。

  ⭐ 为什么单独开一个文件：
     因为原来那份里答案已经在了，放在眼前你迟早会瞟到。
     在这个空文件里写出来 —— 写出来才算你的。

  怎么跑：  .venv\Scripts\python.exe tests\_重写_题8.py
════════════════════════════════════════════════════════════
"""

import os
import csv
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data")


# ============================================================
# 题 8（16 分）综合作战：扫描 + 清洗 + 统计
#
#   输入：data_dir 是存放 CSV 的目录；top_n 是取前几名
#   输出：字典
#
#   正常：  {"total_rows": 90,
#            "n_speakers": 7,
#            "top_speakers": [("访谈者", 18), ("受访者B", 16), ("受访者E", 15)]}
#
#   目录不存在：{"total_rows": 0, "n_speakers": 0, "top_speakers": []}
#
#   要求：
#     1. 只读【interviews 开头 + .csv 结尾】的文件
#     2. 每行是字典，有 "speaker" 和 "text"
#     3. 缺字段、或 text 是空白的行，跳过
#     4. 目录不存在 → 返回空报告
#
#   五步（题面给的）：
#     ① 目录不存在？直接返回空报告
#     ② os.listdir 拿文件名，筛出 interviews*.csv
#     ③ 循环读进来，合并成一个 rows 列表
#     ④ 遍历 rows，跳过不合格的行
#     ⑤ Counter 数 speaker，取前 top_n
# ============================================================
def analyze(data_dir, top_n=3):
    if not os.path.isdir(data_dir):
        return {"total_rows": 0, "n_speakers": 0, "top_speakers": []}

    rows=[]
    for name in os.listdir(data_dir):
        if name.startswith("interview") and name.endswith(".csv"):
            text=os.path.join(data_dir,name)
            with open(text, encoding="utf-8-sig") as f:
                for row in csv.DictReader(f):
                    if "speaker" not in row or "text" not in row:
                        continue
                    if not row["text"].strip():
                        continue
                    rows.append(row)

    counter = Counter(row["speaker"] for row in rows)
    
    return {
    "total_rows": len(rows),
    "n_speakers": len(counter),
    "top_speakers": counter.most_common(top_n),
    }
analyze("E:\\ai\\interview-analysis\\data", top_n=3)

# ============================================================
# 以下不用改 —— 自查
# ============================================================
if __name__ == "__main__":
    print("=" * 62)
    print("  题 8 自查")
    print("=" * 62)

    want_ok = {
        "total_rows": 90,
        "n_speakers": 7,
        "top_speakers": [("访谈者", 18), ("受访者B", 16), ("受访者E", 15)],
    }
    want_empty = {"total_rows": 0, "n_speakers": 0, "top_speakers": []}

    got = analyze(DATA_DIR, top_n=3)
    print("\n① 正常调用 analyze(DATA_DIR, top_n=3)")
    print("   你返回 →", got)
    if got == want_ok:
        print("   ✅ 完全一致")
    else:
        print("   ❌ 期望   →", want_ok)

    miss = analyze(os.path.join(BASE, "不存在的目录"))
    print("\n② 目录不存在 analyze('不存在的目录')")
    print("   你返回 →", miss)
    if miss == want_empty:
        print("   ✅ 完全一致")
    else:
        print("   ❌ 期望   →", want_empty)

    print("\n" + "=" * 62)
    if got == want_ok and miss == want_empty:
        print("  🎉 16 / 16 —— 这 16 分是你的了")
    else:
        print("  还没全对 —— 看上面哪一项对不上，回去改")
    print("=" * 62)
