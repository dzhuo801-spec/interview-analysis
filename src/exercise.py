# 1.
def func(name):
    return f"你叫，{name}"
print(func("小子"))
# 2.
def st(age,num=2):
    return age*num
print(st(3))
print(st(3,4))
# 3.
def li():
    return "我喜欢你",18
print(li())

def li2(nums):
    return max(nums),min(nums)
mai,xiaozi=li2([1,2,3,4,5,6])
print(mai,xiaozi)
# 4
def dic(name):
    print(name)
lis=dic("like")
print(lis)
# 5.
count = 0

def add():
    count = 1
    print(count)

print(add())
print(count)
