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

    # ---------- 下面是留给你填的（本周每天加一条）----------
    # ("练习6: 你的 SQL 标题", """
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
