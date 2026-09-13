"""建 SQL 练习用的数据库

为什么要这个？
→ Python 自带 sqlite3，不用装 MySQL、不用配服务，一条命令就有能写 SQL 的库。
→ 以后你装 MySQL 了，语法 90% 通用，学了不浪费。

运行：py sql/01_setup_db.py
"""
import os
import sqlite3

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "sql", "practice.db")

# 如果已存在就先删掉，保证每次跑出来的数据完全一样（可重复很重要）
if os.path.exists(DB):
    os.remove(DB)

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ============================================================
# 建表
# ============================================================
cur.executescript("""
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS orders;

-- 员工表
CREATE TABLE employees (
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    dept_id     INTEGER,          -- 部门 id，关联 departments.id
    city        TEXT,             -- 城市
    salary      REAL,             -- 月薪
    hire_date   TEXT,             -- 入职日期 'YYYY-MM-DD'
    manager_id  INTEGER           -- 上级 id（指向本表 id）
);

-- 部门表（和员工表是「一对多」关系：一个部门有多个员工）
CREATE TABLE departments (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL,          -- 部门名
    city  TEXT                    -- 部门所在城市
);

-- 订单表（第 3 周做 JOIN 练习用）
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    user_id     INTEGER,          -- 下单用户
    amount      REAL,             -- 金额
    order_date  TEXT
);
""")

# ============================================================
# 插入数据
# ============================================================
departments = [
    (1, "销售部", "北京"),
    (2, "技术部", "北京"),
    (3, "市场部", "上海"),
    (4, "运营部", "上海"),
    (5, "人事部", "广州"),
]
cur.executemany("INSERT INTO departments VALUES (?, ?, ?)", departments)

# (id, name, dept_id, city, salary, hire_date, manager_id)
employees = [
    (1,  "张伟",   1, "北京", 28000, "2018-03-01", None),
    (2,  "李娜",   1, "北京", 22000, "2019-07-15", 1),
    (3,  "王强",   1, "北京", 15000, "2021-01-10", 1),
    (4,  "刘洋",   1, "上海", 18000, "2020-05-20", 1),
    (5,  "陈静",   1, "上海", 12000, "2022-09-01", 4),
    (6,  "赵磊",   1, "广州",  9000, "2023-04-12", 4),
    (7,  "孙丽",   1, "广州", 11000, "2022-11-03", 4),
    (8,  "周涛",   2, "北京", 35000, "2017-06-01", None),
    (9,  "吴敏",   2, "北京", 30000, "2019-02-18", 8),
    (10, "郑凯",   2, "北京", 26000, "2020-08-25", 8),
    (11, "冯雪",   2, "上海", 24000, "2021-03-30", 8),
    (12, "陈鹏",   2, "上海", 20000, "2022-06-15", 11),
    (13, "褚静",   2, "深圳", 19000, "2023-01-09", 11),
    (14, "卫东",   3, "上海", 17000, "2020-10-12", None),
    (15, "蒋雯",   3, "上海", 14000, "2021-09-07", 14),
    (16, "沈杰",   3, "上海", 13000, "2023-03-21", 14),
    (17, "韩雪",   3, "广州", 10000, "2023-08-01", 14),
    (18, "杨帆",   4, "上海", 16000, "2021-05-17", None),
    (19, "朱丹",   4, "上海", 12500, "2022-12-05", 18),
    (20, "秦峰",   4, "深圳",  8000, "2024-02-19", 18),
    (21, "尤佳",   4, "深圳",  9500, "2023-10-08", 18),
    (22, "许飞",   5, "广州", 11000, "2021-07-22", None),
    (23, "何丽",   5, "广州",  8500, "2023-06-14", 22),
    (24, "吕鹏",   5, "广州",  7800, "2024-04-02", 22),
]
cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?)", employees)

# 订单数据（第 3 周 JOIN 用）
orders = [
    (1, 1, 1200.0, "2026-01-05"), (2, 1, 800.0, "2026-01-19"),
    (3, 2, 2500.0, "2026-02-03"), (4, 3, 450.0, "2026-02-11"),
    (5, 3, 3200.0, "2026-03-02"), (6, 5, 600.0, "2026-03-15"),
    (7, 8, 5000.0, "2026-01-22"), (8, 8, 1500.0, "2026-02-28"),
    (9, 9, 900.0, "2026-03-08"), (10, 12, 2200.0, "2026-03-19"),
    (11, 12, 700.0, "2026-04-01"), (12, 14, 1800.0, "2026-04-10"),
    (13, 18, 2600.0, "2026-02-14"), (14, 22, 300.0, "2026-03-25"),
    (15, 22, 1100.0, "2026-04-18"),
]
cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)

conn.commit()

# ============================================================
# 打印结果，确认数据没问题
# ============================================================
print(f"数据库已创建: {DB}\n")

for table in ("employees", "departments", "orders"):
    n = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"  {table:12} {n:3} 行")

print("\n--- 按部门统计人数（用来出练习题）---")
for row in cur.execute("""
    SELECT d.name, COUNT(*) AS 人数
    FROM employees e JOIN departments d ON e.dept_id = d.id
    GROUP BY d.name ORDER BY 人数 DESC
"""):
    print(f"  {row[0]}: {row[1]} 人")

print("\n--- 按城市统计人数 ---")
for row in cur.execute("SELECT city, COUNT(*) FROM employees GROUP BY city ORDER BY 2 DESC"):
    print(f"  {row[0]}: {row[1]} 人")

print("\n--- 按部门+城市统计人数 ---")
for row in cur.execute("""
    SELECT d.name, e.city, COUNT(*) AS n
    FROM employees e JOIN departments d ON e.dept_id = d.id
    GROUP BY d.name, e.city ORDER BY d.name, n DESC
"""):
    print(f"  {row[0]} / {row[1]}: {row[2]} 人")

print("\n--- 工资最高的 5 人 ---")
for row in cur.execute("SELECT name, city, salary FROM employees ORDER BY salary DESC LIMIT 5"):
    print(f"  {row[0]}  {row[1]}  {row[2]:.0f}")

print("\n--- 有上级的人（manager_id 不是 NULL）---")
n = cur.execute("SELECT COUNT(*) FROM employees WHERE manager_id IS NOT NULL").fetchone()[0]
total = cur.execute("SELECT COUNT(*) FROM employees").fetchone()[0]
print(f"  {n} / {total} 人有上级，{total - n} 人没有（是部门负责人）")

conn.close()
print("\n完成。现在可以用 02_practice.py 开始写 SQL 了。")
