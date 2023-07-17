# 比较列表list 和字典 dict 两种内置数据类型上各种操作大O数量级
# 两种都属于容器，都是可变类型。
# 类型    list                         dict
# 索引    自然数i                       不可变类型值key
# 添加    append/extend/insert         b[k]=v
# 删除    pop/remove                   pop
# 更新    a[i]=v                       b[k]=v
# 正查    a[i]/a[i:j]                  b[k]/copy
# 反查    index(v)/count(v)            无
# 其他    reverse/sort                 has_key/update


# List 列表数据类型常用操作性能
# 最常用：按索引取值和赋值（v=a[i],a[i]=v）
# 由于列表的随机访问特性，这两个操作执行时间与列表大小无关，数量级均为O(1)
# 另一个是列表增长，可以选择append()和_add_() "+"
# lst.append(v),执行是将是o(1)
# lst = lst + [v],执行时间是o(n+k),其中k是被加的列表长度 。（本质是生成一个新的列表再复制过去）
# 选择哪个方法来操作列表，决定了程序的性能

# 用+的方式生成
def test1():
    l = []
    for i in range(1000):
        l = l + [i]


# 用append方法添加元素
def test2():
    l = []
    for i in range(1000):
        l.append(i)


# 用列表推导式
def test3():
    l = [i for i in range(1000)]


# 用range函数调用转成列表
def test4():
    l = list(range(1000))


# 用timeit模块对函数进行计数
# 创建一个Timer对象，指定需要反复运行的语句和只需运行一次的安装语句
# 调用这个对象的timeit方法，其中可以指定反复运行多少次

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat %f seconds\n" % t1.timeit(number=1000))

t2 = Timer("test2()", "from __main__ import test2")
print("concat %f seconds\n" % t2.timeit(number=1000))

t3 = Timer("test3()", "from __main__ import test3")
print("concat %f seconds\n" % t3.timeit(number=1000))

t4 = Timer("test4()", "from __main__ import test4")
print("concat %f seconds\n" % t4.timeit(number=1000))


# List操作比较大O()数量级
# index[]       O(1)
# pop()         O(1)
# pop(i)        O(n)
# reverse       O(n)
# sort          O(n log n)


# 我们注意到pop这个操作：
# pop()从末尾移除元素         O(1)
# pop(i)从列表中部移除元素·    O(n)
# 原因在于python所选择的实现方法
# 从中部移除元素的话，要把移除元素后面的元素全部向前挪位复制一边，这个看起来有点笨拙，但这种实现方法能狗保证列表按索引取值和赋值的操作很快，达到O（1）
# 这也是一种对常用和不常用操作的折衷方案


