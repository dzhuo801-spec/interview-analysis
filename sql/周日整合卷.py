"""星期日整合卷 · SQL 第 1 期

════════════════════════════════════════════════════════════
  什么时候做：每周日（总结与复习日）
  怎么做：  在下面 8 个空字符串里写 SQL，然后运行本文件自查
  怎么跑：  .venv\\Scripts\\python.exe sql/周日整合卷.py
  ════════════════════════════════════════════════════════════

  规则：
    [禁止] 不许翻之前的练习文件，不许搜答案
    [OK]  可以翻 SQL语法库.md
    [OK]  目标：8 道题全部 PASS（100 分）

  ⭐ 和平时不一样 —— 平时一题考一个知识点，
     这里**每题都跨 2~3 个知识点**（筛选 + 分组 + 排序 一起用）。

  ⭐ 这 8 道覆盖了第 1 周学的全部 SQL：
     SELECT / WHERE / ORDER BY / LIMIT / IN / BETWEEN / LIKE / IS NULL
     COUNT / SUM / AVG / MAX / MIN / GROUP BY / HAVING
"""

import os
import sqlite3

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "sql", "practice.db")


# ============================================================
# 题 1（12 分）多条件筛选 + 排序
#
# 查出**在北京或上海**、且**工资在 15000 到 30000 之间**的员工，
# 输出 name / city / salary 三列，**按工资从高到低排**。
#
# 涉及：IN / BETWEEN / AND / ORDER BY DESC
# 预期：10 行，第一行是 吴敏 | 北京 | 30000.0
# ============================================================
Q1 = """
SELECT ...
"""


# ============================================================
# 题 2（10 分）IS NULL
#
# 查出**没有上级**（manager_id 是空的）的员工，输出 name 和 salary，
# **按工资从高到低排**。
#
# 涉及：IS NULL（不能用 = NULL）
# 预期：5 行，第一行是 周涛 | 35000.0
# ============================================================
Q2 = """
SELECT ...
"""


# ============================================================
# 题 3（12 分）一条 SQL 出四个统计值
#
# 在**一条** SQL 里同时查出：员工总数、平均工资、最高工资、最低工资。
#
# 涉及：COUNT / AVG / MAX / MIN
# 预期：1 行，24 | 16512.5 | 35000.0 | 7800.0
# ============================================================
Q3 = """
SELECT ...
"""


# ============================================================
# 题 4（13 分）GROUP BY 分组统计
#
# 查出**每个部门**的：部门 id、人数、平均工资。
# **按 dept_id 升序排**。
#
# 涉及：GROUP BY / COUNT / AVG / ORDER BY
# 预期：5 行，第一行 1 | 7 | 16428.57...
# ============================================================
Q4 = """
SELECT ...
"""


# ============================================================
# 题 5（13 分）HAVING 筛分组
#
# 找出**平均工资超过 20000** 的部门，输出 dept_id 和平均工资。
#
# 涉及：GROUP BY / HAVING（不是 WHERE！）
# 预期：1 行，2 | 25666.67
# ============================================================
Q5 = """
SELECT ...
"""


# ============================================================
# 题 6（14 分）WHERE + GROUP BY + HAVING + ORDER BY 四件套
#
# 查出**员工人数超过 3 人**的城市，输出 city / 人数 / 平均工资，
# **按平均工资从高到低排**。
#
# 涉及：GROUP BY / COUNT / AVG / HAVING / ORDER BY DESC
# 预期：3 行，第一行 北京 | 6 | 26000.0
# 提示：深圳只有 3 个人，会被筛掉
# ============================================================
Q6 = """
SELECT ...
"""


# ============================================================
# 题 7（10 分）LIKE + 聚合
#
# 数一数**姓张或姓陈**的员工一共有几个。
#
# 涉及：LIKE + % / OR / COUNT(*)
# 预期：1 行，3
# ============================================================
Q7 = """
SELECT ...
"""


# ============================================================
# 题 8（16 分）⭐ 综合作战题 —— 一份部门薪资报告
#
# 查出**每个部门**的：
#   dept_id / 人数 / 最高工资 / 最低工资 / 平均工资（四舍五入 1 位小数）
# **按平均工资从高到低排**。
#
# 涉及：GROUP BY / COUNT / MAX / MIN / AVG / ROUND / ORDER BY DESC
# 预期：5 行，第一行 2 | 6 | 35000.0 | 19000.0 | 25666.7
# 提示：ROUND(AVG(salary), 1)
# ============================================================
Q8 = """
SELECT ...
"""


# ============================================================
# 以下不用改 —— 自动批改
# ============================================================
def run(sql):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    con.close()
    return cols, rows


def near(a, b, tol=0.01):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return abs(float(a) - float(b)) <= tol
        except (TypeError, ValueError):
            return False
    return a == b


def row_near(got, want):
    if len(got) != len(want):
        return False
    return all(near(g, w) for g, w in zip(got, want))


results = []


def check(no, name, score, want_rows, want_first=None, sort_desc_col=None):
    sql = globals().get(f"Q{no}", "")
    if not sql or "SELECT ..." in sql or len(sql.strip()) < 15:
        results.append((no, name, 0, score, False, "还没写 SQL"))
        return
    try:
        _, rows = run(sql)
    except Exception as e:
        results.append((no, name, 0, score, False, f"{type(e).__name__}: {e}"))
        return
    if len(rows) != want_rows:
        results.append((no, name, 0, score, False,
                        f"应该是 {want_rows} 行，实际 {len(rows)} 行"))
        return
    if want_first is not None and not row_near(rows[0], want_first):
        results.append((no, name, 0, score, False,
                        f"第一行应该是 {want_first}，实际 {rows[0]}"))
        return
    if sort_desc_col is not None:
        vals = [r[sort_desc_col] for r in rows]
        if vals != sorted(vals, reverse=True):
            results.append((no, name, 0, score, False, "没有按要求的列从高到低排序"))
            return
    results.append((no, name, score, score, True, "正确"))


check(1, "多条件筛选：IN + BETWEEN + ORDER BY", 12, 10, ("吴敏", "北京", 30000.0))
check(2, "IS NULL：找没有上级的人", 10, 5, ("周涛", 35000.0))
check(3, "一条 SQL 出四个统计值", 12, 1, (24, 16512.5, 35000.0, 7800.0))
check(4, "GROUP BY：部门人数 + 均薪", 13, 5, (1, 7, 16428.57142857143))
check(5, "HAVING：均薪超 2 万的部门", 13, 1, (2, 25666.666666666668))
check(6, "四件套：人数>3 的城市", 14, 3, ("北京", 6, 26000.0), sort_desc_col=2)
check(7, "LIKE + COUNT：姓张或姓陈", 10, 1, (3,))
check(8, "综合作战：部门薪资报告", 16, 5, (2, 6, 35000.0, 19000.0, 25666.7), sort_desc_col=4)

print("=" * 68)
print("  星期日整合卷 · SQL 第 1 期")
print("=" * 68)
print()

total = 0
full = 0
for no, name, got, mx, ok, msg in results:
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] 题 {no}   {name}")
    print(f"          {got}/{mx} 分   {msg}")
    total += got
    full += mx

print()
print("=" * 68)
print(f"  总分：{total} / {full}")
if total == full:
    print("  *** 全过！第 1 周 SQL 通关")
elif total >= full * 0.7:
    print("  [!] 及格但没全过 —— 把 FAIL 的补掉")
else:
    print("  [X] 没过关 —— 回去翻 SQL语法库.md，下周日重测")
print("=" * 68)
