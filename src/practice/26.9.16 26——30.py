# 26
square=lambda x : x**2
print(square(4))
is_even=lambda x :x%2==0
print(is_even(7))
# 非三元：
bigger=lambda x,y:max(x,y)
print(bigger(3,9))
# 三元
bigger=lambda x,y:x if x>y else y
print(bigger(3,9))
# 27
wc = {"的": 28, "了": 21, "这个": 15, "现在": 14, "都": 10}
def top_n(wc,n):
    wc_items=wc.items()
    return sorted(wc_items,key=lambda x:x[1],reverse=True)[ :n]
print(top_n(wc,3))
# 28
def to_ints(str_list):
    return list(map(int,str_list))
print(to_ints(["1", "2", "3"]))
print(to_ints(["10"]))
print(to_ints([]))
# 29
import os,csv
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path=os.path.join(BASE,"data","interviews.csv")
print(data_path)
with open(data_path,encoding="utf-8-sig") as f:
    rows=list(csv.DictReader(f))
print(len(rows))
print(rows[0])
def long_texts(rows,min_len):
    return list(filter(lambda x:len(x["text"])>min_len,rows))
print(len(long_texts(rows, 12)))
print(long_texts(rows, 12)[0])
# 30 用if来筛选nums，如果有就执行first,*rest = nums，如果没有就直接返回空（none），not是不的意思，判断出来的。
def split_first(nums):
    if not nums:
        return None,[]
    first,*rest = nums
    return first,rest
print(split_first([1,2,3,4,5]))