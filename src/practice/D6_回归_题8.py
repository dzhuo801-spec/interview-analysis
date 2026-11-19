# 用 pandas 重做 SQL 盲区【题 8】：找出「工资高于本部门平均工资」的人
#
#   靶子： (11, 4)  →  列是  name / 部门 / 薪资 / 部门均薪
#
# 数据： E:\ai\interview-analysis\sql\practice.db
#   employees   : id, name, dept_id, city, salary, hire_date, manager_id   (24 行)
#   departments : id, name, city                                          (5 行)
#
# ⚠️ dept_id 是数字（1~5），人看不懂 —— 所以最后要拿 departments 表把数字换成名字。
#    这就是你卡住的那一步。

import sqlite3

import pandas as pd

DB = r"E:\ai\interview-analysis\sql\practice.db"

# ── ① 读两张表 ────────────────────────────────────────────────
conn = sqlite3.connect(DB)
emp = pd.read_sql("SELECT id, name, dept_id, salary FROM employees", conn)
dept = pd.read_sql("SELECT id, name FROM departments", conn)
conn.close()          # ⚠️ 放最后：所有 read_sql 都做完了，才关

print("① emp.shape  ->", emp.shape)      # (24, 4)
print("① dept.shape ->", dept.shape)     # (5, 2)
print()

# ── ② 算【每个部门的平均工资】─────────────────────────────────
#     groupby 把 24 行【压成】5 行：一个部门一个数
#     ⚠️ rename 这一步很关键：先把列名改成"部门均薪"，
#        后面 merge 就不会出现 _x / _y 那种看不懂的后缀了
均薪 = (emp.groupby("dept_id", as_index=False)["salary"].mean()
           .rename(columns={"salary": "部门均薪"}))

print("② 部门均薪（5 行）:")
print(均薪.round(2).to_string(index=False))
print()

# ── ③ 把这 5 个数【贴回】24 行 ────────────────────────────────
#     merge 之后：每个人一行，同时有【我的工资】和【我部门的均薪】
m = emp.merge(均薪, on="dept_id", how="left")
print("③ merge 之后 columns ->", m.columns.tolist())
print(m.head(3).round(2).to_string(index=False))
print()

# ── ④ 筛：谁的工资 > 他部门的均薪 ──────────────────────────────
高于 = m[m["salary"] > m["部门均薪"]]
print("④ 高于本部门均薪的人 ->", len(高于), "行")
print()

# ── ⑤ ⭐⭐ 把 dept_id 换成【部门名】—— 你卡的就是这一步 ─────────
#     思路和刚才一模一样：再 merge 一次，这次拿 departments 表当"字典"
#     departments 的关键列也叫 id / name，跟 emp 撞名，
#     所以先 rename 成 dept_id / 部门，merge 完就不会有 _x _y
dept2 = dept.rename(columns={"id": "dept_id", "name": "部门"})
print("⑤ dept2 columns ->", dept2.columns.tolist())
print(dept2.to_string(index=False))
print()

最终 = 高于.merge(dept2, on="dept_id", how="left")
print("⑤ 链接部门名之后 columns ->", 最终.columns.tolist())
print()

# ── ⑥ 选列 → 靶子 ────────────────────────────────────────────
结果 = 最终[["name", "部门", "salary", "部门均薪"]]
print("⑥ 最终 shape ->", 结果.shape, "   ← 靶子 (11, 4)")
print()
print(结果.round(2).to_string(index=False))
