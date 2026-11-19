"""SQL 盲区专项运行器 —— 补面试最爱考、但你 02_practice.py 里一次都没写过的语法

⚠️ 这是 03，不是 02 —— 02_practice.py 的 83 道练习已经封卷了，别再去动它。
   盲区题单独放这里，做完一样能 git commit，是独立的一份能力证据。

用法：
    1. 往下找到 QUERIES 里「题 N」，把 SQL 填进那对三个引号之间
    2. 运行：.venv\\Scripts\\python.exe sql/03_盲区.py
    3. 看最后一行「自查」—— 行数对不上就是还没写对

题面、要求、实测预期值 → 看 E:\\ai\\python学习\\SQL盲区专项.md
语法不懂 → 看 E:\\ai\\python学习\\SQL语法库.md

"""
import os
import sqlite3

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "sql", "practice.db")

# ============================================================
# 第 1 批：CASE WHEN（10/8 周四 · 6 道全部通过）
# 第 2 批：WITH(CTE) + UNION（10/10 周六 · 5 道全部通过 · 零返工）
# 第 3 批：日期函数（10/11 周日 · 5 道通过，2 处排序 10/13 补齐）
# 第 4 批：LAG / LEAD / ROWS BETWEEN（10/14 周三）
# 第 5 批：文本 / GROUP_CONCAT / 判空 / CAST（10/15 周四）
# 写完记得跑，跑完看最后的「自查」
# 自查只查【行数】—— 真正的门在 SQL盲区专项.md 的「验收」表里
# ============================================================
QUERIES = [
    (1, "按月薪分三档（低 <10000 / 中 10000~20000 / 高 >20000）", """
        SELECT name,salary,CASE WHEN salary<10000 THEN "低" WHEN salary<=20000 THEN "中" WHEN salary>20000 THEN "高" ELSE 0 END AS 档位 FROM employees ORDER BY salary DESC
    """),

    (2, "每个部门：高薪人数(>=20000) + 普通人数", """
        SELECT d.name AS 部门,COUNT(CASE WHEN salary >= 20000 THEN 1 END) AS 高薪人数,COUNT(CASE WHEN salary<20000 THEN 1 END) AS 普通人数 FROM employees e JOIN departments d ON e.dept_id=d.id GROUP BY d.id
    """),

    (3, "行转列：每个城市一行，三列是 低/中/高 的人数", """
        SELECT city AS 城市,COUNT(CASE WHEN salary < 10000 THEN 1 END) AS 低,COUNT(CASE WHEN salary<=20000 AND salary >= 10000 THEN 1 END) AS 中,COUNT(CASE WHEN salary>20000 THEN 1 END) AS 高 FROM employees GROUP BY city 
    """),

    (4, "每个部门：总人数 + 高薪人数 + 高薪占比(%)，占比保留 1 位小数", """
        SELECT d.name AS 部门,COUNT(*) AS 总人数,COUNT(CASE WHEN salary >= 20000 THEN 1 END) AS 高薪人数,ROUND(COUNT(CASE WHEN salary >= 20000 THEN 1 END)*100.0/COUNT(*),1) AS 高薪占比 FROM employees e JOIN departments d ON e.dept_id=d.id GROUP BY d.name ORDER BY dept_id
    """),

    (5, "员工列表，负责人(manager_id 是 NULL)排最前面，同一组内按工资降序", """
        SELECT name,dept_id,manager_id,CASE WHEN manager_id IS NULL THEN "负责人" WHEN manager_id IS NOT NULL THEN "组员" ELSE 0 END AS 角色 FROM employees ORDER BY 角色 DESC,salary DESC
    """),

    (6, "每个员工一行：订单数 + 订单总额；没有订单的显示 0，不许出现 NULL", """
        SELECT e.name,COUNT(o.user_id) AS 订单数,CASE WHEN SUM(o.amount) IS NULL THEN 0 WHEN SUM(o.amount) IS NOT NULL THEN SUM(o.amount) END AS 订单总额 FROM employees e LEFT JOIN orders o ON e.id=o.user_id GROUP BY e.name ORDER BY SUM(amount) DESC
    """),

    # ---------- 第 2 批：WITH(CTE) + UNION（10/10 周六）----------
    (7, "CTE 入门：工资高于【全公司】平均工资的人", """
        WITH 全公司 AS (SELECT AVG(salary) AS 均薪 FROM employees)
        SELECT name,salary FROM employees WHERE salary > (SELECT 均薪 FROM 全公司) ORDER BY salary DESC
    """),

    (8, "CTE + JOIN：工资高于【本部门】平均工资的人", """
        WITH 部门均薪 AS (SELECT dept_id,AVG(salary) AS 均薪 FROM employees GROUP BY dept_id)
        SELECT e.name,d.name AS 部门,e.salary AS 薪资,x.均薪 AS 部门均薪 FROM employees e JOIN 部门均薪 x ON e.dept_id=x.dept_id JOIN departments d ON e.dept_id=d.id WHERE salary > x.均薪
    """),

    (9, "两个 CTE 串起来：人数 >= 5 且 均薪 > 15000 的部门", """
        WITH 部门均薪 AS (SELECT dept_id,AVG(salary) AS 均薪 FROM employees GROUP BY dept_id),
             部门人数 AS (SELECT dept_id,COUNT(*) AS 人数 FROM employees GROUP BY dept_id)
        SELECT d.name AS 部门,x.人数,ROUND(z.均薪,2) AS 均薪 FROM departments d JOIN 部门均薪 z ON z.dept_id=d.id JOIN 部门人数 x ON x.dept_id=d.id WHERE x.人数 >=5 AND z.均薪 >15000 ORDER BY d.id
    """),

    (10, "UNION ALL：高薪(>=25000) 和 负责人 竖着拼（带「来源」列，不去重）", """
        SELECT name,salary,'高薪' AS 来源 FROM employees WHERE salary>=25000 UNION ALL SELECT name,salary,'负责人' AS 来源 FROM employees WHERE manager_id IS NULL 
    """),

    (11, "UNION 去重：同样两拨人，只留 name 和 salary（不许重复）", """
        SELECT name,salary FROM employees WHERE salary>=25000 UNION SELECT name,salary FROM employees WHERE manager_id IS NULL ORDER BY salary DESC 
    """),

    # ---------- 第 3 批：日期函数（10/11 周日）----------
    # 语法看 E:\ai\python学习\SQL语法库.md  §8 → 日期
    (12, "STRFTIME 入门：按入职年份数人头", """
        SELECT STRFTIME('%Y', hire_date) AS 年,COUNT(*) AS 人数 FROM employees GROUP BY 年 ORDER BY 年
    """),

    (13, "按月统计订单：月份 + 订单数 + 总金额", """
        SELECT STRFTIME('%Y-%m',order_date) AS 年月,COUNT(*) AS 订单数,SUM(amount) AS 总金额 FROM orders GROUP BY 年月 ORDER BY 年月
    """),

    (14, "日期区间：2026 年 2~3 月的订单（含 3/31）", """
        SELECT * FROM orders WHERE order_date >='2026-02-01' AND order_date <='2026-03-31' ORDER BY order_date ASC
    """),

    (15, "入职年限：截至 2026-10-11 的整年数（生日陷阱）", """
        SELECT name,hire_date,CAST((JULIANDAY('2026-10-11') - JULIANDAY(hire_date)) / 365.25 AS INT) AS 工龄 FROM employees ORDER BY 工龄 DESC, hire_date ASC
    """),

    (16, "星期几：统计订单落在周几，翻成中文", """
        SELECT CASE WHEN STRFTIME('%w',order_date) == '0' THEN '周日' WHEN STRFTIME('%w',order_date) == '1' THEN '周一' WHEN STRFTIME('%w',order_date) == '2' THEN '周二' WHEN STRFTIME('%w',order_date) == '3' THEN '周三' WHEN STRFTIME('%w',order_date) == '4' THEN '周四' WHEN STRFTIME('%w',order_date) == '5' THEN '周五' WHEN STRFTIME('%w',order_date) == '6' THEN '周六' ELSE 0 END AS 周几,COUNT(*) AS 订单数,SUM(amount)FROM orders GROUP BY 周几 ORDER BY 订单数 DESC,STRFTIME('%w',order_date) ASC
    """),

    # ---------- 第 4 批：LAG / LEAD / ROWS BETWEEN（10/14 周三）----------
    # 语法看 E:\ai\python学习\SQL语法库.md  §7 窗口函数 后面新加的三节
    (17, "LAG 入门：每张订单 + 上一单金额", """
        SELECT id,order_date,amount,LAG(amount) OVER(ORDER BY order_date ASC) AS 上一单金额 FROM orders ORDER BY order_date ASC
    """),

    (18, "按月环比：月份 + 总额 + 上月总额 + 环比增幅", """
        WITH 月总额 AS (SELECT STRFTIME('%Y-%m',order_date) AS 月份,SUM(amount) AS 总额 FROM orders GROUP BY 月份)
        SELECT 月份,总额,LAG(总额) OVER(ORDER BY 月份) AS 上月总额,ROUND((总额-LAG(总额) OVER(ORDER BY 月份))*100/LAG(总额) OVER(ORDER BY 月份),1) AS 环比增幅 FROM 月总额
    """),

    (19, "LEAD：下一单日期 + 距下一单天数", """
        SELECT id,order_date,amount,LEAD(order_date) OVER(ORDER BY order_date) AS 下一单日期,CAST(JULIANDAY(LEAD(order_date) OVER(ORDER BY order_date))-JULIANDAY(order_date) AS INT) AS 距下一单天数 FROM orders ORDER BY order_date ASC
    """),

    (20, "近 3 单移动平均（ROWS BETWEEN）", """
        SELECT id,order_date,amount,AVG(amount) OVER(ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS 近3单均值 FROM orders
    """),

    (21, "累计金额（ROWS BETWEEN UNBOUNDED PRECEDING）", """
        SELECT id,order_date,amount,SUM(amount) OVER(ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS 累计 FROM orders
    """),

    (22, "PARTITION BY + LAG：每个用户相邻两单间隔天数", """
        WITH 下过两单 AS (SELECT user_id,order_date,LAG(order_date) OVER(PARTITION BY user_id ORDER BY order_date) AS 上一单日期 FROM orders)
        SELECT user_id,上一单日期,order_date,CAST(JULIANDAY(order_date)-JULIANDAY(上一单日期) AS INT) AS 间隔天数 FROM 下过两单 WHERE 上一单日期 IS NOT NULL
    """),

    # ---------- 第 5 批：文本 / GROUP_CONCAT / 判空 / CAST（10/15 周四）----------
    # 语法看 E:\ai\python学习\SQL语法库.md  §9（新加的那一节）
    (23, "拼接 ||：姓名(部门)", """
        SELECT e.name || '(' || d.name || ')' AS 标签 FROM employees e JOIN departments d ON e.dept_id = d.id ORDER BY e.id ASC
    """),

    (24, "字符串函数：字数 / 姓 / 替换 / 查找", """
        SELECT name,LENGTH(name) AS 字数,SUBSTR(name,1,1) AS 性,REPLACE(name,"静","晶") AS 替换后,INSTR(name,"雪") AS 位置 FROM employees
    """),

    (25, "GROUP_CONCAT：每个部门有谁（成员按 id 升序拼）", """
        SELECT d.name AS 部门,GROUP_CONCAT(e.name,"、") FROM employees e JOIN departments d ON e.dept_id = d.id GROUP BY d.name ORDER BY e.id ASC,d.id ASC
    """),

    (26, "GROUP_CONCAT + 条件拼接：每个部门的高薪成员（没有 → 无）", """
        SELECT d.name AS 部门,COALESCE(GROUP_CONCAT(CASE WHEN salary>=20000 THEN e.name END,"、"),'无') AS 高新人员 FROM employees e JOIN departments d ON e.dept_id = d.id GROUP BY d.name ORDER BY e.id ASC,d.id ASC 
    """),

    (27, "判空：负责人显示「无」", """
        SELECT name,dept_id,manager_id,COALESCE(GROUP_CONCAT(CASE WHEN manager_id IS NULL THEN "无" END),manager_id) AS 上级 FROM employees GROUP BY name ORDER BY id ASC
    """),

    (28, "CAST：类型转换 6 连问（不需要 FROM）", """
        SELECT CAST('123' AS INTEGER)+1 AS a,
               CAST(3.99 AS INTEGER)    AS b,
               ROUND(3.99,1)            AS c,
               CAST(12 AS TEXT) || "元" AS d,
               CAST('abc' AS INTEGER)   AS e,
               CAST('12abc' AS INTEGER) AS f
    """),
]

# ============================================================
# 自查表：每道题「正确答案有几行」
# 这个数字是拿参考答案在 practice.db 上实测出来的，不是估的
# ============================================================
EXPECT_ROWS = {
    1: 24,
    2: 5,
    3: 4,
    4: 5,
    5: 24,
    6: 24,
    7: 10,
    8: 11,
    9: 2,
    10: 9,
    11: 7,
    12: 8,
    13: 4,
    14: 9,
    15: 24,
    16: 7,
    17: 15,
    18: 4,
    19: 15,
    20: 15,
    21: 15,
    22: 5,
    23: 24,
    24: 24,
    25: 5,
    26: 5,
    27: 24,
    28: 1,
}


def show(cursor, rows):
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
    print(f"  -> 共 {len(rows)} 行")


def main():
    if not os.path.exists(DB):
        print(f"找不到数据库 {DB}")
        print("先运行：.venv\\Scripts\\python.exe sql/01_setup_db.py")
        return

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    done = 0
    passed = 0
    todo = []

    for num, title, sql in QUERIES:
        print("=" * 70)
        print(f"【题 {num}】{title}")
        print("=" * 70)

        if "TODO" in sql:
            print("  [--] 还没写（把 -- TODO 那一行删掉，换成你的 SQL）")
            todo.append(num)
            print()
            continue

        done += 1
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            show(cur, rows)

            want = EXPECT_ROWS.get(num)
            if want is None:
                pass
            elif len(rows) == want:
                print(f"  [OK] 行数对：{len(rows)} 行")
                passed += 1
            else:
                print(f"  [X ] 行数不对：你 {len(rows)} 行，应该是 {want} 行")
                if len(rows) < want:
                    print("       少行最常见的原因：JOIN 用成了 INNER，把没人/没订单的那几行吃掉了")
                else:
                    print("       多行最常见的原因：你按 A 分组，但 SELECT 里还带了 B 的列")
        except Exception as e:
            print(f"  [X ] 报错: {type(e).__name__}: {e}")
            print(f"       你的 SQL: {sql.strip()}")
        print()

    print("=" * 70)
    print(f"写了 {done}/{len(QUERIES)} 题，【行数】自查通过 {passed}/{len(QUERIES)} 题")
    if todo:
        print("还没写：" + "、".join(f"题 {n}" for n in todo))
    print()
    print("!! 上面只查了【行数】，没查【内容】—— 行数对 != 全对。")
    print("   这一步只是第一道门。真正的门在 SQL盲区专项.md 的「验收」表里。")
    print("   → 回去把每一题的「验收」逐条打勾，打完了再告诉我。")
    print()
    print("   已经有过好几次“行数过了但内容是错的”—— 别让它再发生：")
    print("     题 1  看三档人数（5/13/6），不是看“24 行”")
    print("     题 3  看每一行的数加起来是不是 = 总人数")
    print("     题 4  看【小数位】对不对")
    print("     题 5  看第 1 名是谁")
    print("     题 6  看有没有 None、总额是不是 SUM 出来的")
    print("     题 8  看部门均薪对不对（销售部 16428.57）")
    print("     题 9  应该只有 2 个部门（想清楚为什么不是 5 个）")
    print("     题 10 张伟要出现【两次】")
    print("     题 11 张伟只能出现【一次】—— 两次就去看题库第 11 题的「坑」")
    print()
    print("   ---- 第 3 批（日期函数）----")
    print("     题 12 应该 8 行（按年份），出 24 行说明忘了 GROUP BY")
    print("     题 13 月份必须是 '2026-01' 这种 —— 只写 %m 的话跨年就错")
    print("     题 14 是 9 行，而且别用 STRFTIME 包住 order_date（索引会失效）")
    print("     题 15 卫东必须是 5 年；算出 6 就是用了“年份相减”")
    print("     题 16 周日那行总额必须是 1500 —— 0 是周日，不是周一")
    print()
    print("   ---- 第 4 批（LAG / LEAD / ROWS BETWEEN）----")
    print("     题 17 第一行必须是 NULL（没有上一行），第二行才是 1200")
    print("     题 18 四行是 7000 / 7050 / 7200 / 3600，环比 0.7 / 2.1 / -50.0")
    print("     题 19 全部天数的合计必须是 103（最后一行没有下一单）")
    print("     题 20 第 3 行 2333.3、第 4 行 2766.7 —— 窗口要会“滑”")
    print("     题 21 最后一行必须 = 24850（跟全表总额对得上）")
    print("     题 22 是 5 行，而且必须用 PARTITION BY（不然跨用户取上一单）")
    print()
    print("   ---- 第 5 批（文本 / GROUP_CONCAT / 判空 / CAST）----")
    print("     题 23 第 1 行 张伟(销售部)、最后一行 吕鹏(人事部)，括号必须是英文 ()")
    print("     题 24 张伟 → 2 / 张 / 张伟 / 0；陈静、褚静 → 陈晶、褚晶；冯雪、韩雪 → 位置 2")
    print("     题 25 顺序不能靠默认！ORDER BY 要写进 GROUP_CONCAT 括号里面")
    print("     题 26 市场/运营/人事 三行必须是「无」—— 少了说明 LEFT JOIN 写成 INNER 了")
    print("     题 27 正好 5 行「无」：张伟、周涛、卫东、杨帆、许飞")
    print("     题 28 a=124 b=3 c=4.0 d=12元 e=0 f=12 —— b 是取整、c 才是四舍五入")

    conn.close()


if __name__ == "__main__":
    main()
