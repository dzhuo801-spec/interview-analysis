"""day1.py —— 读数据 → 统计 → 出图（D1 的最小可用版本）

运行：.venv\\Scripts\\python.exe src/day1.py

[!] 运行命令的坑（2026-09-13 实测更正，别搞错）
    这个项目【一律用 .venv 的解释器】，原因是：

      python  命令        → 完全不能用：0 字节商店空壳，退出码 9009
      py src/day1.py     → 会崩：py 指向全局 Python，只有 4 个包
                            → ModuleNotFoundError: No module named 'matplotlib'
      .venv\\Scripts\\python.exe src/day1.py  → ✅ 正确（matplotlib/jieba 都在这）

    你可能还记得"用 py 不要用 python" —— 那条仍然对，但对本项目不够：
    py 只能跑纯标准库的脚本，一旦用到 pandas / matplotlib / jieba 就必须用 venv。

[!] 这个文件里有几处标着 TODO，是要你自己写的。
   读完全部代码，理解每一行，再把 TODO 补上。
   补不上来 → 问我「为什么」，别问「答案是什么」。
"""
import csv
import os
from collections import Counter

# matplotlib 的两行必备设置（不写，图里中文全是方框）
import matplotlib
matplotlib.use("Agg")                    # 不弹窗口，直接存文件
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 项目根目录（这样路径不受你在哪运行影响）
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ============ 1. 读取数据 ============
def read_data(filepath):
    """读取 CSV，返回一个列表，每个元素是一行（字典形式）

    为什么要写成函数？
    → 因为「读文件」这件事你以后每个项目都要做。写一次，到处用。
    → 这就是"写脚本"和"写程序"的区别。
    """
    rows = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)       # 每行变成字典，键 = 表头
        for row in reader:
            rows.append(row)
    return rows


# ============ 2. 统计每个说话人说了几句 ============
def count_by_speaker(rows):
    """统计每个说话人的句子数，返回 Counter"""
    counter = Counter()
    for row in rows:
        # Counter 支持直接 += 1，不存在这个键就自动从 0 开始
        counter[row["speaker"]] += 1
    return counter


# ============ 3. 词频统计（中文要分词！）============
def count_words(rows):
    """把所有发言分词后统计词频，返回 Counter

    [!] 关键知识点：中文不能用 split() 切分！
       因为中文词与词之间没有空格，"我们这边的婚俗" 会被当成一整个词。
       所以要用 jieba（中文分词库）。
    """
    import jieba                      # 放在函数里 import 也行，但通常写在文件顶部

    words = []
    for row in rows:
        # jieba.lcut() 把一句话切成词列表，例如：
        # "我们这边的婚俗" → ['我们', '这边', '的', '婚俗']
        words += jieba.lcut(row["text"])
    return Counter(words)


# ============ 4. 出图 ============
def plot_bar(counter, top_n, title, outpath, color="#4C8BF5"):
    """画水平条形图并保存"""
    most_common = counter.most_common(top_n)
    # most_common 返回 [(词, 次数), ...]，这里把两个字段拆开
    labels = [item[0] for item in most_common]      # 列表推导式
    values = [item[1] for item in most_common]

    # 水平柱状图的标签是从下往上排的，反转一下让它从上往下读
    labels.reverse()
    values.reverse()

    fig, ax = plt.subplots(figsize=(8, top_n * 0.35 + 1.5))
    ax.barh(labels, values, color=color)
    ax.set_title(title)
    ax.set_xlabel("次数")

    # 在柱子末端标数字
    for i, v in enumerate(values):
        ax.text(v + 0.3, i, str(v), va="center")

    fig.tight_layout()
    fig.savefig(outpath, dpi=100)
    plt.close(fig)                   # 关掉，不然图多了会占内存
    return outpath


# ============ 主流程 ============
if __name__ == "__main__":
    # 所有路径都用相对项目根目录的写法
    data_path = os.path.join(BASE, "data", "interviews.csv")
    out_dir = os.path.join(BASE, "output")
    os.makedirs(out_dir, exist_ok=True)

    # 1. 读
    rows = read_data(data_path)
    print(f"共读入 {len(rows)} 条记录\n")

    # 2. 看着一眼数据长什么样（好习惯：拿到数据先看，别急着分析）
    print("前 3 条记录：")
    for row in rows[:3]:
        print("  ", row)
    print()

    # 3. 谁说得最多
    speaker_count = count_by_speaker(rows)
    print("每个人说了几句：")
    for name, count in speaker_count.most_common():
        print(f"  {name}: {count} 句")
    print()

    # 4. 词频（先看原始结果，包括没意义的词）
    word_count = count_words(rows)
    print(f"总共 {sum(word_count.values())} 个词，不重复的有 {len(word_count)} 个")
    print("出现最多的 15 个词：")
    for word, count in word_count.most_common(15):
        print(f"  {word}: {count} 次")
    print()

    # 5. 出两张图
    p1 = plot_bar(speaker_count, top_n=4,
                  title="各说话人发言句数",
                  outpath=os.path.join(out_dir, "speaker_count.png"),
                  color="#4C8BF5")
    p2 = plot_bar(word_count, top_n=15,
                  title="词频 Top 15（未去停用词）",
                  outpath=os.path.join(out_dir, "word_freq.png"),
                  color="#F5A623")

    print("图已生成：")
    print("  ", p1)
    print("  ", p2)


# ================================================================
# TODO（明天做，不是今天的）
# ----------------------------------------------------------------
# TODO 1：停用词过滤
#   上面词频图里会出现「的」「了」「是」「我们」这些没意义的词。
#   做法：准备一个停用词列表，过滤掉它们。
#   stopwords = ["的", "了", "是", "我", "你", "他", "在", "和", "就", "都"]
#   → 思考：过滤该放在 count_words() 里面，还是外面？为什么？
#
# TODO 2：算每个人平均每句话多少字
#   提示：len(字符串) 得长度。先算每个人的总字数，再除以句数。
#
# TODO 3：把统计结果保存成 CSV
#   用 csv.writer 写出一个新的 CSV 文件（想一想：这个功能该写成函数吗？）
#
# TODO 4：数据里如果有空的 text（缺失值），现在会怎样？
#   去 data/interviews.csv 里手动删掉几行 text，再跑一次看看。
#   然后想：应该丢弃还是填充？为什么？
# ================================================================
