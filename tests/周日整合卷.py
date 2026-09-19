"""星期日整合卷 · 第 1 期

════════════════════════════════════════════════════════════
  什么时候做：每周日（总结与复习日）
  怎么做：  把每题下面的 TODO 补完，然后运行本文件自查
  怎么跑：  .venv\\Scripts\\python.exe tests/周日整合卷.py
  ════════════════════════════════════════════════════════════

  规则：
    [禁止] 不许看 day1.py，不许搜答案，不许看之前的题
    [OK]  可以翻 Python代码笔记.md
    [OK]  目标：8 道题全部 PASS（100 分）

  ⭐ 这份卷子和平时的题不一样 ——
     平时一题考一个知识点，这里**每题都跨 3~5 个知识点**，
     模拟真实工作里"几个东西串起来用"的感觉。

  ⭐ 这 8 道题合起来，覆盖了你第 1 周学的全部内容：
     字符串 / 列表 / 字典 / 循环 / 函数 / 默认参数 / 多返回值
     lambda / map / filter / sorted(key=) / Counter
     文件读写 / CSV 读写 / 异常处理 / 拆包 / import
"""

import csv
import os
from collections import Counter

# ============================================================
# 题 1（10 分）字典累加 + lambda 排序 + 切片
#
# 写 top_chars(text, n)
#   输入：text 是字符串；n 是整数
#   输出：出现次数最多的 n 个字符，形如 [('a', 2), ('b', 2)]
#         （列表里装元组，按次数从高到低）
#
# 要求：
#   1. 用普通 dict 手动累加（[禁止] 用 Counter）
#   2. 用 sorted(key=lambda ...) 排序（[禁止] 用 most_common）
#   3. n 大于实际字符种类数时，返回全部（不报错）
#
# 涉及知识点：循环 / 字典 get 累加 / lambda / sorted / 切片
# ============================================================
def top_chars(text, n):
    # TODO: 你写这里
    pass


# ============================================================
# 题 2（10 分）函数多返回值 + 拆包 + 边界防御
#
# 写 min_max_avg(nums)
#   输入：数字列表
#   输出：元组 (最小值, 最大值, 平均值)
#   边界：nums 是空列表时，返回 (None, None, 0)
#
# 要求：调用时能这样写 —— lo, hi, avg = min_max_avg([1, 2, 3, 4])
#
# 涉及知识点：函数返回多值（其实是元组）/ 拆包 / 边界情况 / 除法
# ============================================================
def min_max_avg(nums):
    # TODO: 你写这里
    pass


# ============================================================
# 题 3（12 分）列表推导 + filter + map + lambda + 异常
#
# 写 clean_square(items)
#   输入：混合列表，形如 ["1", "2", "abc", "4", "5", ""]
#   输出：把能转成整数的挑出来 → 只留偶数 → 每个平方
#
# 要求：
#   1. "abc" 和 "" 转不了整数，**要跳过，不能崩**（用 try/except）
#   2. 奇数的平方不要（1 和 5 都去掉）
#   3. **必须用 filter 和 map**（不许全用 for 循环写）
#
# 涉及知识点：异常处理 / filter / map / lambda / 类型转换
# ============================================================
def clean_square(items):
    # TODO: 你写这里
    # 提示：分三步 —— ①先全转成 int（转不了的记成 None）②去掉 None ③filter+map
    pass


# ============================================================
# 题 4（12 分）Counter + 拆包 + 排序
#
# 写 word_ranking(texts, n)
#   输入：texts 是字符串列表；n 是整数
#   输出：出现次数最多的 n 个词，形如 [('a', 3), ('b', 2)]
#
# 要求：
#   1. 用 split() 分词（不用 jieba）
#   2. 用 Counter 统计（可以先把多个 Counter 加起来）
#   3. n 比词数大时返回全部
#
# 涉及知识点：Counter / += 合并 / most_common / split
# ============================================================
def word_ranking(texts, n):
    # TODO: 你写这里
    pass


# ============================================================
# 题 5（14 分）文件读写 + strip + 列表推导
#
# 写 read_lines(path)
#   输入：文件路径
#   输出：列表 —— 每行内容（**去掉首尾空白**），**空行跳过**
#   边界：文件不存在时返回 []
#
# 要求：
#   1. 用 with open 写法，编码 utf-8
#   2. 用 strip() 去空白
#   3. 空行不放进结果
#   4. 文件不存在不能崩（用 try/except）
#
# 涉及知识点：with open / strip / 列表推导 / 异常 / 边界
# ============================================================
def read_lines(path):
    # TODO: 你写这里
    pass


# ============================================================
# 题 6（14 分）CSV 读 + 字典累加 + 排序
#
# 写 count_by_field(csv_path, field)
#   输入：CSV 路径；field 是列名
#   输出：字典 {该列的值: 出现次数}，**按次数从高到低**（Python 3.7+ 字典保序）
#   边界：文件不存在时返回 {}
#
# 要求：
#   1. 用 csv.DictReader 读，**必须加 encoding="utf-8-sig"**
#   2. 该列 strip() 后为空的行要跳过
#   3. 用普通 dict 手动累加（[禁止] 用 Counter）
#
# 涉及知识点：csv.DictReader / utf-8-sig / 字典累加 / 异常 / 排序
# ============================================================
def count_by_field(csv_path, field):
    # TODO: 你写这里
    pass


# ============================================================
# 题 7（12 分）CSV 写 + 编码 + 目录
#
# 写 save_pairs(pairs, path)
#   输入：pairs 是 [('词', 次数), ...] 这样的列表；path 是目标路径
#   输出：写入的数据行数（**不含表头**）
#
# 要求：
#   1. 用 csv.writer，三个参数一个不能少：w / utf-8-sig / newline=""
#   2. 第一行是表头：词,次数
#   3. 路径的上级目录不存在时，**自动创建**
#
# 涉及知识点：csv.writer / utf-8-sig / newline / os.makedirs / 拆包遍历
# ============================================================
def save_pairs(pairs, path):
    # TODO: 你写这里
    # 提示：for word, count in pairs:  ← 这是循环里拆包
    pass


# ============================================================
# 题 8（16 分）⭐ 综合作战题 —— 最像真实工作的一题
#
# 写 analyze(data_dir, top_n=3)
#   输入：data_dir 是存放 CSV 的目录；top_n 是取前几名
#   输出：一个字典，形如：
#        {
#          "total_rows": 90,                  # 合并后的总行数
#          "n_speakers": 7,                   # 说话人种类数
#          "top_speakers": [("访谈者", 18), ...]  # 发言最多的前 top_n 个
#        }
#
# 要求：
#   1. 扫描 data_dir，读取**文件名以 "interviews" 开头、以 ".csv" 结尾**的文件，全部合并
#   2. 每行是个字典，有 "speaker" 和 "text" 两个字段
#   3. **缺字段、或者 text 是空白的行，要跳过**（健壮性）
#   4. 目录不存在时返回 {"total_rows": 0, "n_speakers": 0, "top_speakers": []}
#
# 涉及知识点：os.listdir / os.path.join / startswith / endswith
#             csv 读 / 字典 get / Counter / most_common / 异常 / 默认参数
# ============================================================
def analyze(data_dir, top_n=3):
    # TODO: 你写这里
    # 提示：这一步一步来 ——
    #   ① 目录不存在？直接返回空报告
    #   ② os.listdir 拿到文件名，筛出 interviews*.csv
    #   3 个文件 for 循环读进来，合并成一个 rows 列表
    #   ③ 遍历 rows，跳过不合格的行
    #   ④ Counter 数 speaker，取前 top_n
    pass


# ============================================================
# 以下不用改 —— 自动批改
# ============================================================
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data")
TMP_DIR = os.path.join(BASE, "tests", "_tmp")

results = []


def check(name, score, fn):
    try:
        ok, msg = fn()
        results.append((name, score if ok else 0, score, ok, msg))
    except Exception as e:
        results.append((name, 0, score, False, f"抛异常了: {type(e).__name__}: {e}"))


def t1():
    got = top_chars("aabbc", 2)
    if not isinstance(got, list):
        return False, f"应该返回列表，实际是 {type(got).__name__}（忘了 return？）"
    if got != [("a", 2), ("b", 2)] and got != [["a", 2], ["b", 2]]:
        return False, f"top_chars('aabbc', 2) 期望 [('a',2),('b',2)]，实际 {got}"
    got2 = top_chars("abc", 10)
    if len(got2) != 3:
        return False, f"n 比实际字符种类多时应该返回全部 3 个，实际 {len(got2)} 个"
    if top_chars("", 3) != []:
        return False, "空字符串应该返回空列表"
    return True, "正确"


def t2():
    r = min_max_avg([1, 2, 3, 4])
    if not isinstance(r, tuple) or len(r) != 3:
        return False, f"应该返回 3 个值的元组，实际 {r!r}"
    lo, hi, avg = r
    if (lo, hi, avg) != (1, 4, 2.5):
        return False, f"min_max_avg([1,2,3,4]) 期望 (1, 4, 2.5)，实际 {(lo, hi, avg)}"
    e = min_max_avg([])
    if e != (None, None, 0):
        return False, f"空列表期望 (None, None, 0)，实际 {e!r}"
    lo2, hi2, avg2 = min_max_avg([7])
    if (lo2, hi2, avg2) != (7, 7, 7):
        return False, f"单个元素期望 (7, 7, 7)，实际 {(lo2, hi2, avg2)}"
    return True, "正确"


def t3():
    got = clean_square(["1", "2", "abc", "4", "5", ""])
    if got != [4, 16]:
        return False, f"期望 [4, 16]，实际 {got}"
    if clean_square([]) != []:
        return False, "空列表应该返回空列表"
    if clean_square(["abc", "x", ""]) != []:
        return False, "全是非法值时应该返回空列表（不能崩）"
    if clean_square(["2.5"]) != []:
        return False, "'2.5' 不是整数，应该跳过（int() 会抛 ValueError）"
    return True, "正确"


def t4():
    got = word_ranking(["a b a", "b c a"], 2)
    if got != [("a", 3), ("b", 2)] and got != [["a", 3], ["b", 2]]:
        return False, f"期望 [('a',3),('b',2)]，实际 {got}"
    got2 = word_ranking(["x y"], 10)
    if len(got2) != 2:
        return False, f"n 比词数大时应该返回全部 2 个，实际 {len(got2)} 个"
    if word_ranking([], 3) != []:
        return False, "空输入应该返回空列表"
    return True, "正确"


def t5():
    os.makedirs(TMP_DIR, exist_ok=True)
    path = os.path.join(TMP_DIR, "t5.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("第一行\n\n  第二行  \n第三行\n\n")
    got = read_lines(path)
    if got != ["第一行", "第二行", "第三行"]:
        return False, f"期望 3 行且去掉了空白，实际 {got!r}"
    if read_lines(os.path.join(TMP_DIR, "没有这个.txt")) != []:
        return False, "文件不存在时应该返回 []（不能崩）"
    return True, "正确"


def t6():
    got = count_by_field(os.path.join(DATA_DIR, "interviews.csv"), "speaker")
    if not isinstance(got, dict):
        return False, f"应该返回字典，实际 {type(got).__name__}"
    if len(got) != 4:
        return False, f"应该有 4 个说话人，实际 {len(got)} 个: {list(got)}"
    if got.get("受访者B") != 16:
        return False, f"受访者B 应该是 16，实际 {got.get('受访者B')}"
    if list(got.values()) != sorted(got.values(), reverse=True):
        return False, f"结果应该按次数从高到低排列，实际顺序 {list(got.items())}"
    if count_by_field(os.path.join(DATA_DIR, "不存在.csv"), "speaker") != {}:
        return False, "文件不存在时应该返回 {}（不能崩）"
    return True, "正确"


def t7():
    os.makedirs(TMP_DIR, exist_ok=True)
    target = os.path.join(TMP_DIR, "新建的子目录", "t7.csv")
    n = save_pairs([("的", 28), ("了", 21)], target)
    if n != 2:
        return False, f"应该返回数据行数 2（不含表头），实际 {n}"
    if not os.path.exists(target):
        return False, "文件没写出来（父目录没自动创建？）"
    with open(target, encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if rows[0] != ["词", "次数"]:
        return False, f"表头应该是 ['词','次数']，实际 {rows[0]}"
    if rows[1] != ["的", "28"] or rows[2] != ["了", "21"]:
        return False, f"数据行不对，实际 {rows[1:]}"
    return True, "正确"


def t8():
    got = analyze(DATA_DIR, top_n=3)
    if not isinstance(got, dict):
        return False, f"应该返回字典，实际 {type(got).__name__}"
    for key in ("total_rows", "n_speakers", "top_speakers"):
        if key not in got:
            return False, f"返回的字典缺少字段: {key}"
    if got["total_rows"] != 90:
        return False, f"总行数应该是 90（50+40），实际 {got['total_rows']}"
    if got["n_speakers"] != 7:
        return False, f"说话人应该 7 种，实际 {got['n_speakers']}"
    tops = got["top_speakers"]
    if len(tops) != 3:
        return False, f"top_n=3 应该返回 3 个，实际 {len(tops)}"
    if tops[0][0] != "访谈者" or tops[0][1] != 18:
        return False, f"第一名应该是 ('访谈者', 18)，实际 {tops[0]}"
    counts = [c for _, c in tops]
    if counts != sorted(counts, reverse=True):
        return False, "top_speakers 应该按次数从高到低"
    miss = analyze(os.path.join(BASE, "不存在的目录"))
    if miss != {"total_rows": 0, "n_speakers": 0, "top_speakers": []}:
        return False, f"目录不存在时期望空报告，实际 {miss!r}"
    return True, "正确"


# ---------- 跑起来 ----------
print("=" * 68)
print("  星期日整合卷 · 第 1 期")
print("=" * 68)
print()

check("题 1   字典累加 + lambda 排序 + 切片", 10, t1)
check("题 2   多返回值 + 拆包 + 边界防御", 10, t2)
check("题 3   异常 + filter + map + lambda", 12, t3)
check("题 4   Counter + 拆包 + 排序", 12, t4)
check("题 5   文件读写 + strip + 列表推导", 14, t5)
check("题 6   CSV 读 + 字典累加 + 排序", 14, t6)
check("题 7   CSV 写 + 编码 + 建目录", 12, t7)
check("题 8   综合作战：扫描 + 清洗 + 统计", 16, t8)

total = 0
full = 0
for name, got, mx, ok, msg in results:
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] {name}")
    print(f"         {got}/{mx} 分   {msg}")
    total += got
    full += mx

print()
print("=" * 68)
print(f"  总分：{total} / {full}")
if total == full:
    print("  *** 全过！第 1 周通关，可以进第 2 周")
elif total >= full * 0.7:
    print("  [!] 及格了但没全过 —— 把 FAIL 的补掉再进下周")
else:
    print("  [X] 没过关 —— 回去补这周的内容，下周日重测")
print("=" * 68)
