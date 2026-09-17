# # 1.
# def func(name):
#     return f"你叫，{name}"
# print(func("小子"))
# # 2.
# def st(age,num=2):
#     return age*num
# print(st(3))
# print(st(3,4))
# # 3.
# def li():
#     return "我喜欢你",18
# print(li())
#
# def li2(nums):
#     return max(nums),min(nums)
# mai,xiaozi=li2([1,2,3,4,5,6])
# print(mai,xiaozi)
# # 4
# def dic(name):
#     print(name)
# lis=dic("like")
# print(lis)
# # 5.
# count = 0
#
# def add():
#     count = 1
#     print(count)
#
# print(add())
# print(count)

# 1.我个人觉得，因为[]列表，是属于可填入的，但None是不可变的，本身该函数里面参数属于默认参数，如果没有被修改就返回默认参数，修改了，才会表示更改的参数
# 第一个因为，cart已经被定义成None,而且还通过判断cart是否在None地址，如果是属于None就返回并填入列表，但是又因为函数参数是根据位置对应的，所以无论如何都不会修改cart的值
# 又因为is必须是同一个内存地址才行，所以被修改后的cart自然就不会被返回，只有满足同一个地址才能执行，所以每次执行时候，列表数据都只有一个
# 但第二个，你因为默认参数是cart=[]，但由于列表是可填入的，每次返回并填入时候，列表也会发生改变，导致列表的数会越来越多。
def add_item(item, cart=None):    # ✅
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print(add_item("苹果"))
print(add_item("香蕉"))
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("苹果"))    # → ['苹果']
print(add_item("香蕉"))    # → ['苹果', '香蕉']  ← 你以为是 ['香蕉']！
# 2.第一个函数是可变参数，一般以元组形式接收，第二个函数是关键字参数,一般以字典形式接收
def total(*args):
    return sum(args)

print(total(1, 2, 3))

def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

show(name="张三", age=20)
# 3.global全球，全部之意，把函数之外的total也包含进来了，第一次输入80时候，使之外面的total变成了80，第二次输入90时候，把total加上90，成为170
total = 0
def add_score(score):
    global total          # ← 声明要改全局变量
    total += score
add_score(80)
add_score(90)
print(total)              # → 170