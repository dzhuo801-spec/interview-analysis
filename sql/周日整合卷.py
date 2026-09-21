"""星期日整合卷 · SQL 第 1 期

════════════════════════════════════════════════════════════
  什么时候做：每周日（总结与复习日）
  怎么做：  在下面 8 个空字符串里写 SQL，然后运行本文件自查
  怎么跑：  .venv\\Scripts\\python.exe sql/周日整合卷.py
  ════════════════════════════════════════════════════════════

  规则：
    [禁止] 不许翻之前的练习文件，不许搜答案
    [OK]  可以翻 SQL语法库.md
    [OK]  目标：≥70 分算过，100 分是全对

  ⭐ 和平时不一样 —— 平时一题考一个知识点，
     这里**每题都跨 2~3 个知识点**（筛选 + 分组 + 排序 一起用）。

  ⭐ 每题都给了【示例】—— 告诉你应该查出几行、长什么样。
     写完跑一遍就知道对不对。

  ⭐ 这 8 道覆盖了第 1 周学的全部 SQL：
     SELECT / WHERE / ORDER BY / LIMIT / IN / BETWEEN / LIKE / IS NULL
     COUNT / SUM / AVG / MAX / MIN / GROUP BY / HAVING

  📁 数据库：sql/practice.db
     employees 24 行 / departments 5 行 / orders 15 行
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
# 【示例】应该查出 10 行，长这样（前 5 行）：
#
#     name  | city | salary
#     ------+------+--------
#     吴敏  | 北京 | 30000.0     ← 第一行是这个
#     张伟  | 北京 | 28000.0
#     郑凯  | 北京 | 26000.0
#     冯雪  | 上海 | 24000.0
#     李娜  | 北京 | 22000.0
#     ...
#
# 【涉及】IN / BETWEEN / AND / ORDER BY DESC
# ============================================================
Q1 =("""
    SELECT name,city,salary FROM employees WHERE salary BETWEEN 15000 AND 30000 AND(city IN ('北京','上海')) ORDER BY salary DESC
    """)
# ============================================================
# 题 2（10 分）IS NULL
#
# 查出**没有上级**（manager_id 是空的）的员工，输出 name 和 salary，
# **按工资从高到低排**。
#
# 【示例】应该查出 5 行，长这样：
#
#     name | salary
#     -----+--------
#     周涛 | 35000.0     ← 第一行
#     张伟 | 28000.0
#     卫东 | 17000.0
#     杨帆 | 16000.0
#     许飞 | 11000.0
#
# 【涉及】IS NULL（⚠️ 不能用 `= NULL`，那样查出来是 0 行）
# ============================================================
Q2 =("""
SELECT name,salary FROM employees WHERE manager_id IS NULL ORDER BY salary DESC
""")


# ============================================================
# 题 3（12 分）一条 SQL 出四个统计值
#
# 在**一条** SQL 里同时查出：员工总数、平均工资、最高工资、最低工资。
#
# 【示例】应该查出 1 行：
#
#     COUNT(*) | AVG(salary) | MAX(salary) | MIN(salary)
#     ---------+-------------+-------------+------------
#     24       | 16512.5     | 35000.0     | 7800.0
#
# 【涉及】COUNT / AVG / MAX / MIN（四个一起写，不分行）
# ============================================================
Q3 =("""
SELECT COUNT(*),AVG(salary),MAX(salary),MIN(salary) FROM employees
""")


# ============================================================
# 题 4（13 分）GROUP BY 分组统计
#
# 查出**每个部门**的：部门 id、人数、平均工资。
# **按 dept_id 升序排**。
#
# 【示例】应该查出 5 行：
#
#     dept_id | 人数 | 均薪
#     --------+------+----------
#     1       | 7    | 16428.57     ← 第一行
#     2       | 6    | 25666.67
#     3       | 4    | 13500.0
#     4       | 4    | 11500.0
#     5       | 3    | 9100.0
#
#     【验算】人数加起来 = 7+6+4+4+3 = 24 ✅（正好是员工总数）
#
# 【涉及】GROUP BY / COUNT / AVG / ORDER BY
# 【提示】GROUP BY 后面写 dept_id（要分组的那一列）
# ⚠️ 这题的小数**保留 2 位**（跟示例一致）。**不要**写 ROUND(AVG(salary), 1)
#    —— 那是第 8 题的要求，写这会差 0.03 被判错。不写 ROUND、原样输出也是对的。
# ============================================================
Q4 =("""
SELECT dept_id,COUNT(dept_id) AS 人数,AVG(salary) AS 均新 FROM employees GROUP BY dept_id ORDER BY dept_id ASC
""")


# ============================================================
# 题 5（13 分）HAVING 筛分组
#
# 找出**平均工资超过 20000** 的部门，输出 dept_id 和平均工资。
#
# 【示例】应该查出 1 行：
#
#     dept_id | AVG(salary)
#     --------+-------------
#     2       | 25666.67
#
#     【为什么只有 1 行】各部门均薪：1→16428 / 2→25666 / 3→13500
#                        4→11500 / 5→9100，只有部门 2 超过 20000
#
# 【涉及】GROUP BY / HAVING
# ⚠️ **必须用 HAVING，不能用 WHERE**（WHERE 里不能写聚合函数）
# ⚠️ 小数**保留 2 位**（跟示例一致），同样**不要**用 ROUND(..., 1)。
# ============================================================
Q5 =("""
SELECT dept_id,avg(salary) FROM employees GROUP BY dept_id HAVING AVG(salary)>20000 
""")


# ============================================================
# 题 6（14 分）WHERE + GROUP BY + HAVING + ORDER BY 四件套
#
# 查出**员工人数超过 3 人**的城市，输出 city / 人数 / 平均工资，
# **按平均工资从高到低排**。
#
# 【示例】应该查出 3 行：
#
#     city | 人数 | 均薪
#     -----+------+----------
#     北京 | 6    | 26000.0      ← 第一行（均薪最高）
#     上海 | 9    | 16277.78
#     广州 | 6    | 9550.0
#
#     【为什么深圳没了】深圳只有 3 个人，被 HAVING 筛掉了
#
# 【涉及】GROUP BY / COUNT / AVG / HAVING / ORDER BY DESC
# ============================================================
Q6 =("""
    SELECT city,COUNT(city) AS 人数,AVG(salary) AS 均薪 FROM employees GROUP BY city HAVING COUNT(city)>3 ORDER BY AVG(salary) DESC
    """)


# ============================================================
# 题 7（10 分）LIKE + 聚合
#
# 数一数**姓张或姓陈**的员工一共有几个。
#
# 【示例】应该查出 1 行：
#
#     COUNT(*)
#     --------
#     3
#
#     【哪 3 个】张伟 / 陈静 / 陈鹏
#
# 【涉及】LIKE + % / OR / COUNT(*)
# 【提示】`name LIKE '张%' OR name LIKE '陈%'`
# ============================================================
Q7 =("""
SELECT COUNT(*) FROM employees WHERE name LIKE '张%' OR name LIKE '陈%'
""")


# ============================================================
# 题 8（16 分）⭐ 综合作战题 —— 一份部门薪资报告
#
# 查出**每个部门**的：
#   dept_id / 人数 / 最高工资 / 最低工资 / 平均工资（四舍五入 1 位小数）
# **按平均工资从高到低排**。
#
# 【示例】应该查出 5 行：
#
#     dept_id | 人数 | 最高    | 最低    | 均薪
#     --------+------+---------+---------+---------
#     2       | 6    | 35000.0 | 19000.0 | 25666.7    ← 第一行（均薪最高）
#     1       | 7    | 28000.0 | 9000.0  | 16428.6
#     3       | 4    | 17000.0 | 10000.0 | 13500.0
#     4       | 4    | 16000.0 | 8000.0  | 11500.0
#     5       | 3    | 11000.0 | 7800.0  | 9100.0
#
# 【涉及】GROUP BY / COUNT / MAX / MIN / AVG / ROUND / ORDER BY DESC
# 【提示】
#   - 四舍五入 1 位小数：ROUND(AVG(salary), 1)
#   - 排序用 AVG(salary) 或它的别名都行
# ============================================================
Q8 =("""
    SELECT dept_id,COUNT(dept_id) AS 人数,MAX(salary) AS 最高,MIN(salary) AS 最低,ROUND(AVG(salary),1) AS 均薪 FROM employees GROUP BY dept_id ORDER BY avg(salary) DESC
    """)


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
