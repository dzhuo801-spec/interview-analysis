import os,csv
def safe_load_csv(path, default=None):
    if default is None:
        default = []
    try:
        with open(path, encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:    # ④ 坏情况 A：文件不在
        print(f"找不到文件：{path}")
        return default
    except UnicodeDecodeError:   # ⑤ 坏情况 B：文件在，但编码坏了
        print("找不到文件")
        return default
P = r"E:\ai\interview-analysis\data\interviews.csv"
NO = r"E:\ai\interview-analysis\data\没有这个.csv"
print(safe_load_csv(P))
print(safe_load_csv(NO))
print(safe_load_csv(NO, default=-1))