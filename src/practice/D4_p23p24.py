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
# 31
def pair_up(names, scores):
    return dict(zip(names,scores))
def find_index(items, target):
    for i,n in enumerate(items):
        if n == target:
            return i
    return -1

print(pair_up(["张伟", "李娜", "王强"], [88, 95, 72]))
print(find_index(["a", "b", "c"], "b"))
print(find_index(["a", "b", "c"], "z"))
# 32 在函数中与赋值时不同，在函数中收集是元组，在赋值时候解包是列表。**在函数中是字典，属于关键字参数
def show_args(*args, **kwargs):
    return args,kwargs
print(show_args(1, 2, 3, x=4, y=5))
# 33
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
def safe_index(items, i):
    try:
        return items[i]
    except IndexError:
        return None
print(to_int("42"))
print(to_int("abc"))
print(to_int(""))

print(safe_index([1,2,3], 1))
print(safe_index([1,2,3], 9))
# 34
class NegativeError(Exception):
    pass
def sqrt_approx(x):
    if x>=0:
        return x**0.5
    else:
        raise NegativeError(f"不能对负数开平方:{x}")
try:
    print(sqrt_approx(9))
    print(sqrt_approx(-4))
except NegativeError as e:
    print("接住了：",e)


