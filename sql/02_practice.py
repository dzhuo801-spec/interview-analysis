"""SQL 练习运行器 —— 你写 SQL，它帮你跑

用法：
    1. 改下面 QUERIES 里的 SQL 语句
    2. 运行：.venv\Scripts\python.exe sql/02_practice.py
    3. 看输出结果对不对

为什么要这个？
→ 比在 sqlite 命令行里打方便，而且你的 SQL 能存下来、能 git commit。
→ 面试官看到你 repo 里有系统的 SQL 练习记录，这就是能力证据。
"""
import os
import sqlite3

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "sql", "practice.db")

# ============================================================
# 在这里写你的 SQL（每天做完练习就往这里加）
# ============================================================
QUERIES = [
    # ---------- 9/14 周一：SELECT / FROM / LIMIT ----------
    ("练习1: 查出所有员工", """
        SELECT * FROM employees
    """),

    ("练习2: 只查姓名和工资两列", """
        SELECT name, salary FROM employees
    """),

    ("练习3: 查前 5 个员工", """
        SELECT * FROM employees LIMIT 5
    """),

    ("练习4: 跳过前 5 个，再查 5 个（第 6~10 个）", """
        SELECT * FROM employees LIMIT 5 OFFSET 5
    """),

    ("练习5: 查出所有部门", """
        SELECT * FROM departments
    """),
    ("练习6：查出姓名+城市","""
        SELECT name,city FROM employees
    """),
    ("练习7：查工资最高的3人","""
        SELECT name,salary FROM employees ORDER BY salary DESC LIMIT 3
    """),
    ("练习8:查所有部门名","""
        SELECT name FROM departments 
    """),
    ("练习9：定表单前3名","""
        SELECT * FROM orders LIMIT 3
    """),
    ("练习10：查出所有北京员工","""
        SELECT name,city FROM employees WHERE city = '北京' 
    """),
    ("练习11：查出工资大于 20000 的员工姓名和工资","""
        SELECT name,salary FROM employees WHERE salary >20000
    """),
    ("练习12：查出工资在 10000 到 20000 之间的员工","""
        SELECT name,salary FROM employees WHERE salary BETWEEN 10000 AND 20000
    """),
    ("练习13：查出没有上级的员工（manager_id 是空的）","""
        SELECT name,manager_id FROM employees WHERE manager_id IS NULL
    """),
    # NULL表示未知
    ("练习14：查出姓张的员工","""
       SELECT name FROM employees WHERE name LIKE '张%'
   """),
    ("练习16：用 IN 查多个城市","""
     SELECT name,city FROM employees WHERE city in ('北京','上海')
    """),
    ("练习17：括号别省（AND + OR）","""
     SELECT name,city,salary FROM employees WHERE salary > 20000 AND (city ='北京' OR city='上海')
    """),
    ("练习18：_ 和 % 的区别","""
     SELECT name FROM employees WHERE name LIKE '__'
    """),
    ("练习18.2：_ 和 % 的区别","""
     SELECT name FROM employees WHERE name LIKE '___'
    """),
    ("练习18.3：_ 和 % 的区别","""
     SELECT name FROM employees WHERE name LIKE '陈%'
    """),
    ("练习19：= NULL 为什么查不出东西","""
     SELECT name,manager_id FROM employees WHERE manager_id =NULL
    """),
    # 因为NULL不是空值，它是未知，当你等于的时候，他就只能返回不知道，没有，而且NULL只能使用is与not is来判断书写
    ("练习19.2：= NULL 为什么查不出东西","""
     SELECT name,manager_id FROM employees WHERE manager_id IS NULL
    """),
    ("练习19.3：= NULL 为什么查不出东西","""
     SELECT name,manager_id FROM employees WHERE manager_id IS NOT NULL
    """),
    ("练习20：= 数一共有几个员工","""
     SELECT COUNT(*) FROM employees 
    """),
    ("练习21：= COUNT(*) vs COUNT(列)","""
     SELECT COUNT(*),COUNT(manager_id) FROM employees 
    """),
    ("练习22：= 数有几个不同的城市","""
     SELECT COUNT(DISTINCT(city)) FROM employees 
    """),
    ("练习23：= 平均工资","""
     SELECT AVG(salary) FROM employees
     """),
    ("练习24:最高和最低工资：","""
     SELECT MAX(salary),min(salary) FROM employees
     """),
    ("练习25：工资总和 ","""
     SELECT sum(salary) FROM employees
     """),
    ("练习25：自己验算","""
    SELECT sum(salary)/COUNT(*)FROM employees
    """),
    ("练习26：最高和最低差多少","""
     SELECT max(salary)-min(salary) FROM employees
     """),
    ("练习27：订单表统计","""
     SELECT COUNT(*),sum(amount),sum(amount)/COUNT(*)FROM orders
     """),
    ("练习28：每个部门几个人","""
     SELECT dept_id,COUNT(*) AS 人数 FROM employees GROUP BY dept_id
     """),
    # AS 后面加你自己想要的命令名
    ("练习29：每个城市平均工资（降序）","""
     SELECT city,avg(salary) AS 平均工资 FROM employees GROUP BY city ORDER BY avg(salary) DESC
     """),
    ("练习30：每个部门最高工资","""
     SELECT dept_id,MAX(salary) AS 最高工资 FROM employees GROUP BY dept_id
     """),
    ("练习31：人数超过 4 人的部门","""
     SELECT dept_id,COUNT(dept_id) FROM employees GROUP BY dept_id HAVING COUNT(dept_id)>4
     """),
    ("练习32：平均工资超过 20000 的城市","""
     SELECT city,avg(salary) AS 平均工资 FROM employees GROUP BY city HAVING avg(salary)>20000
     """),
    # ("练习32.2：平均工资超过 20000 的城市","""
    #  SELECT city,avg(salary) AS 平均工资 FROM employees WHERE avg(salary)>20000 GROUP BY city
    # """),
    # OperationalError: misuse of aggregate: avg()不能使用
    ("练习33：一条 SQL 出三列统计","""
     SELECT dept_id,COUNT(dept_id) AS 人数,avg(salary) AS 均薪,max(salary) AS 最高 FROM employees GROUP BY dept_id
     """),
    ("练习34：各城市人数（降序）","""
     SELECT city,COUNT(city) AS 人数 FROM employees GROUP BY city ORDER BY COUNT(city) DESC
     """),
    #
    #     SELECT ...
    # """),
]


# ============================================================
# 运行器（不用改）
# ============================================================
def show(cursor, rows):
    """把查询结果打印成对齐的表格"""
    if cursor.description is None:
        print("  （这条语句没有返回结果）")
        return
    cols = [d[0] for d in cursor.description]
    print("  " + " | ".join(f"{c:<12}" for c in cols))
    print("  " + "-" * (15 * len(cols)))
    for row in rows:
        cells = []
        for v in row:
            if isinstance(v, float):
                cells.append(f"{v:<12.1f}")
            else:
                cells.append(f"{str(v):<12}")
        print("  " + " | ".join(cells))
    print(f"  → 共 {len(rows)} 行")


def main():
    if not os.path.exists(DB):
        print(f"找不到数据库 {DB}")
        print("先运行：.venv\\Scripts\\python.exe sql/01_setup_db.py")
        return

    conn = sqlite3.connect(DB)
    conn.row_factory = None
    cur = conn.cursor()

    ok = 0
    for title, sql in QUERIES:
        print("=" * 70)
        print(f"【{title}】")
        print("=" * 70)
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            show(cur, rows)
            ok += 1
        except Exception as e:
            print(f"  [X] 报错: {type(e).__name__}: {e}")
            print(f"     你的 SQL: {sql.strip()}")
        print()

    print("=" * 70)
    print(f"完成：{ok}/{len(QUERIES)} 条执行成功")
    if ok < len(QUERIES):
        print("有报错的先修好，别跳过 —— 报错信息会告诉你问题在哪")

    conn.close()


if __name__ == "__main__":
    main()
