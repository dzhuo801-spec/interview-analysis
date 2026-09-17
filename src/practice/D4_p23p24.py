# 1
from collections import Counter
def count_chars(s):
    return Counter(s)
print(count_chars("apple")["p"])
# 2
def first_n(list1,num):
    return (list1[ :num])
print(first_n([10, 20, 30, 40], 2))
print(first_n([1, 2], 5))
print(first_n([], 3))
# 3
def sum_manually(nums):
    s=0
    for i in nums:
        s+=i
    return s
print(sum_manually([1, 2, 3, 4]))
print(sum_manually([]))
# 4
def is_long(text, n=10):
    te=len(text)
    return te>n
print(is_long("这句话很长很长很长很长很长"))
print(is_long("短", 5))
print(is_long("12345", 5))
# 5
import os, csv
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(BASE, "data", "interviews.csv"), encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
print(type(rows))
print(len(rows))
def count_by_field(rows, field):
    d={}
    for p in rows:
        v=p[field]
        d[v]=d.get(v,0)+1
    return d
print(count_by_field(rows, "speaker"))
# 6
def find_max(rows, field):
    return max(rows,key=lambda x:int(x[field]))
print(find_max(rows, "id"))
# 7
def filter_rows(rows, field, value):
    return list(filter(lambda x:x[field]==value,rows))
print(filter_rows(rows, "speaker", "受访者A"))