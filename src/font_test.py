"""字体测试 —— 确认 matplotlib 能正常画中文

运行方式：py src/font_test.py
（注意：是 py，不是 python！）
"""
import os

# ⚠️ 关键：先指定 matplotlib 的缓存目录，否则可能报
# "Could not save font_manager cache [Errno 13] Permission denied"。
# 必须在 import matplotlib 之前设置！
# 注意：如果运行环境禁止写入用户主目录，把这行注释掉即可（只是警告，不影响画图）。
os.environ.setdefault("MPLCONFIGDIR", os.path.join(os.path.expanduser("~"), ".matplotlib"))

import matplotlib
matplotlib.use("Agg")          # 不弹窗口，直接存文件（服务器/脚本里都这么用）
import matplotlib.pyplot as plt

# ⚠️ 中文显示的两行必备设置（不写这两行，图里的中文全是方框 □□□）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False   # 解决负号显示成方块的问题

# 准备数据
names = ["访谈者", "受访者A", "受访者B", "受访者C"]
counts = [12, 20, 18, 9]

# 画图
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(names, counts, color="#4C8BF5")
ax.set_title("中文测试：每人发言句数")
ax.set_xlabel("说话人")
ax.set_ylabel("句数")

# 在柱子顶上标数字
for i, v in enumerate(counts):
    ax.text(i, v + 0.3, str(v), ha="center")

fig.tight_layout()

# 保存（路径用相对路径，保证别人 clone 下来也能跑）
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "font_test.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100)

print("图片已生成:", out)
print("打开看看：中文有没有变成方框？")
