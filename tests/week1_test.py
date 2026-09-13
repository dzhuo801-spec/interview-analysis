"""第 1 周周测（9/20 做）

规则：
  [禁止] 不许看 day1.py，不许搜答案
  [OK] 写完运行：.venv\Scripts\python.exe tests/week1_test.py
  [OK] 目标：6 道题全部 PASS

每题下面的 `TODO` 就是你要写的地方。写完后运行本文件自查。
"""
import csv
import os
from collections import Counter

# ============================================================
# 题 1（10 分）：基础函数 + 列表推导式
# 写一个函数 filter_by_salary(rows, min_salary)
#   输入：rows 是员工列表，每个元素是字典，形如 {'name': '张伟', 'salary': 28000}
#   输出：工资 >= min_salary 的员工列表
# 要求：用列表推导式实现（不许用 for + append）
# ============================================================
def filter_by_salary(rows, min_salary):
    # TODO: 你写这里
    # 提示：return [r for r in rows if ...]
    pass


# ============================================================
# 题 2（15 分）：Counter + lambda 排序
# 写一个函数 top_words(texts, n)
#   输入：texts 是字符串列表；n 是整数
#   输出：出现次数最多的 n 个 [词, 次数] 组成的列表，按次数从高到低
# 要求：
#   1. 用 split() 分词（这题不用 jieba，用空格分隔的文本）
#   2. 用 collections.Counter 统计
#   3. 用 sorted(..., key=lambda ...) 排序（不许用 most_common）
# 示例：top_words(["a b a", "b c a"], 2) → [['a', 3], ['b', 2]]
# ============================================================
def top_words(texts, n):
    # TODO: 你写这里
    # 第一步：把所有字符串 split() 后合并成一个词列表
    # 第二步：Counter 统计
    # 第三步：sorted 按次数降序，取前 n 个，转成 [词, 次数] 形式
    pass


# ============================================================
# 题 3（15 分）：异常处理
# 写一个函数 safe_int(text, default=0)
#   输入：任意字符串
#   输出：能转成整数就返回整数；转不了就返回 default
# 要求：
#   1. 用 try/except 实现
#   2. [禁止] 不许用 if text.isdigit() 这种判断绕过异常
#   3. 只捕获 ValueError，不要用裸 except
# 示例：safe_int("123") → 123    safe_int("abc", -1) → -1
# ============================================================
def safe_int(text, default=0):
    # TODO: 你写这里
    pass


# ============================================================
# 题 4（15 分）：文件写入
# 写一个函数 save_lines(lines, filepath)
#   输入：lines 是字符串列表；filepath 是目标文件路径
#   输出：写入的行数（整数）
# 要求：
#   1. 用 with open 写法
#   2. 编码用 utf-8
#   3. 每行末尾要有换行符
# ============================================================
def save_lines(lines, filepath):
    # TODO: 你写这里
    pass


# ============================================================
# 题 5（20 分）：读 CSV + 手动累加
# 写一个函数 count_by_field(csv_path, field)
#   输入：CSV 文件路径；field 是列名（字符串）
#   输出：一个字典 {该列的值: 出现次数}
# 要求：
#   1. 用 csv.DictReader 读取
#   2. 只统计 field 列非空（strip() 后不为空）的行
#   3. 用普通 dict 手动累加（不用 Counter）
#   4. 文件不存在时返回空字典 {}
# 提示：累加用 d[k] = d.get(k, 0) + 1
# ============================================================
def count_by_field(csv_path, field):
    # TODO: 你写这里
    pass


# ============================================================
# 题 6（25 分）：综合题 [*] 最像真实工作的一题
# 写一个函数 analyze_interviews(data_dir, top_n=5)
#   输入：data_dir 是存放 CSV 的目录；top_n 是取前几名
#   输出：一个字典，形如：
#        {
#          "total_rows": 90,                       # 总行数
#          "n_speakers": 7,                        # 说话人种类数
#          "top_speakers": [["受访者B", 20], ...]    # 发言最多的前 top_n 个
#        }
# 要求：
#   1. 读取目录下所有以 "interviews" 开头、以 ".csv" 结尾的文件，合并
#   2. 每行 dict 里有 "speaker" 和 "text" 两个字段
#   3. 缺字段、空文本的行要跳过（健壮性）
#   4. 目录不存在时返回 {"total_rows": 0, "n_speakers": 0, "top_speakers": []}
# 提示：os.listdir() 列文件名，os.path.join() 拼路径，
#      name.startswith() / name.endswith() 判断文件名
# ============================================================
def analyze_interviews(data_dir, top_n=5):
    # TODO: 你写这里
    pass


# ============================================================
# 以下不用改 —— 自动批改
# ============================================================
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data")
TMP_DIR = os.path.join(BASE, "tests", "_tmp")

results = []


def check(name, score, fn):
    """跑一道题的测试函数，记录结果"""
    try:
        ok, msg = fn()
        results.append((name, score if ok else 0, score, ok, msg))
    except Exception as e:
        results.append((name, 0, score, False, f"抛异常了: {type(e).__name__}: {e}"))


def t1():
    rows = [{"name": "A", "salary": 10000}, {"name": "B", "salary": 25000},
            {"name": "C", "salary": 20000}]
    got = filter_by_salary(rows, 20000)
    if not isinstance(got, list):
        return False, f"应该返回列表，实际是 {type(got).__name__}（函数里忘了 return？）"
    names = sorted(x["name"] for x in got)
    if names != ["B", "C"]:
        return False, f"期望 ['B','C']，实际 {names}"
    if filter_by_salary(rows, 99999) != []:
        return False, "没有符合条件的人时应该返回空列表"
    return True, "正确"


def t2():
    got = top_words(["a b a", "b c a"], 2)
    if got != [["a", 3], ["b", 2]] and got != [("a", 3), ("b", 2)]:
        return False, f"期望 [['a',3],['b',2]]，实际 {got}"
    got2 = top_words(["x y"], 5)
    if len(got2) != 2:
        return False, "n 大于实际词数时，应该返回全部词（不是报错）"
    return True, "正确"


def t3():
    if safe_int("123") != 123:
        return False, "safe_int(\"123\") 应该是 123"
    if safe_int("abc", -1) != -1:
        return False, "safe_int(\"abc\", -1) 应该是 -1"
    if safe_int("abc") != 0:
        return False, "默认值应该是 0"
    if safe_int("  42  ") != 42:
        return False, "带空格的 \"  42  \" 应该也能转（int() 本身就支持）"
    return True, "正确"


def t4():
    os.makedirs(TMP_DIR, exist_ok=True)
    path = os.path.join(TMP_DIR, "t4.txt")
    n = save_lines(["第一行", "第二行", "第三行"], path)
    if n != 3:
        return False, f"应该返回写入行数 3，实际 {n}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if content != "第一行\n第二行\n第三行\n":
        return False, f"文件内容不对，实际读到: {content!r}"
    return True, "正确"


def t5():
    got = count_by_field(os.path.join(DATA_DIR, "interviews.csv"), "speaker")
    if not isinstance(got, dict):
        return False, f"应该返回字典，实际 {type(got).__name__}"
    if sum(got.values()) != 50:
        return False, f"interviews.csv 有 50 行，统计总数应该是 50，实际 {sum(got.values())}"
    if len(got) != 4:
        return False, f"应该有 4 个说话人，实际 {len(got)} 个: {list(got)}"
    empty = count_by_field(os.path.join(DATA_DIR, "不存在的文件.csv"), "speaker")
    if empty != {}:
        return False, "文件不存在时应该返回空字典 {}"
    return True, "正确"


def t6():
    got = analyze_interviews(DATA_DIR, top_n=3)
    if not isinstance(got, dict):
        return False, f"应该返回字典，实际 {type(got).__name__}"
    for key in ("total_rows", "n_speakers", "top_speakers"):
        if key not in got:
            return False, f"返回的字典缺少字段: {key}"
    if got["total_rows"] != 90:
        return False, f"总行数应该是 90（50+40），实际 {got['total_rows']}"
    if got["n_speakers"] != 7:
        return False, f"说话人应该 7 种，实际 {got['n_speakers']}"
    if len(got["top_speakers"]) != 3:
        return False, f"top_n=3 应该返回 3 个，实际 {len(got['top_speakers'])}"
    counts = [c for _, c in got["top_speakers"]]
    if counts != sorted(counts, reverse=True):
        return False, "top_speakers 应该按次数从高到低排序"
    miss = analyze_interviews(os.path.join(BASE, "不存在的目录"))
    if miss["total_rows"] != 0:
        return False, "目录不存在时 total_rows 应该是 0"
    return True, "正确"


# ---------- 跑起来 ----------
print("=" * 66)
print("  第 1 周周测")
print("=" * 66)
print()

check("题 1  基础函数 + 列表推导式", 10, t1)
check("题 2  Counter + lambda 排序", 15, t2)
check("题 3  异常处理 try/except", 15, t3)
check("题 4  文件写入 with open", 15, t4)
check("题 5  读 CSV + 手动累加", 20, t5)
check("题 6  综合：批量读取 + 统计", 25, t6)

total = 0
full = 0
for name, got, mx, ok, msg in results:
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] {name}")
    print(f"         得分 {got}/{mx}   {msg}")
    total += got
    full += mx

print()
print("=" * 66)
print(f"  总分：{total} / {full}")
if total == full:
    print("  *** 全过！第 1 周通关，可以进第 2 周")
elif total >= full * 0.7:
    print("  [!] 及格但没全过 —— 把 FAIL 的题补掉再进下周")
else:
    print("  [X] 没过关 —— 回去补这周的内容，下周一重测")
print("=" * 66)
