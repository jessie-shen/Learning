# 所谓的变位词，是指两个词之间存在组成字母的重新排列关系
# 如heart, earth, python,typhon
# 简单起见，假设参与判断的两个词仅有小写字母构成，且长度相等

# 解题目标：写一个bool函数，以两个词作为参数，返回这两个词是否变位词

# 解法一：
# 将词1中的字符逐个到词2去检查是否存在，存在就打勾，防止重复检查，如果每个字符都能找到，则两个词是变位词，只要有一个字符找不到，就不是变位词。

# 我的写法：
def check_in_01(character1, character2):
    if len(character1) == len(character2):
        length = len(character1)
        for i in character1:
            if i in character2:
                print(f"{i}存在")
            else:
                print(f"{i}不存在")
                break
    else:
        print("请输入字符相同的两个字符串")


# check_in_01('earth', 'hearl')   #我的写法的数量级其实和下面的一样


def anagramSolution(s1, s2):
    alist = list(s2)  # 复制s2到列表    python的字符串是不可变类型
    pos1 = 0  # s1的下标位置
    stikkOK = True  # 是否变位词的标记
    while pos1 <len(s1) and stikkOK:
        pos2 = 0  # s2的下标位置
        found = False  # 是否找得到的标记
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:   # s1的抽出每个字符，该字符和s2的每个字符逐个对比
                found = True   # 是否能找得到的标记
            else:
                pos2 = pos2 +1
        if found:
            alist[pos2] = None  # 如果s1的字符在s2中能找到，那么这个s1字符变成None
        else:
            stikkOK =False
        pos1 =pos1 + 1
    return stikkOK

# 分析算法的复杂度：
# 主要部分在于两重循环，总执行次数=1+2+3...+n n*(n+1)/2=1/2*(n^2) + 1/2*n
# 数量级位O（n^2）级

# 解法2：先排序再比较
# 将两个字符串都按照字母的顺序排好序，再逐个对比是否相同

def anagramSolution2(s1, s2):
    alist1 = list(s1)   # python的字符串是不可变类型,要转成列表
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
        return matches

print(anagramSolution2('abcde', 'acedb'))

# 算法分析
# 最多执行n次，数量级是O（n）
# 但前面的两个sort并不是无代价的。
# 排序的算法运行时间的数量级差不多是O(n^2)或者O(n log n),大过循环的O(n)
# 本算法的运行时间数量级就等于排序过程的数量级O(n log n) ！

# 解法3：暴力解法
# 穷尽所有可能的组合
# 将s1中出现的字符进行全排列，再查看s2是否出现再全排列中
# 这里最大的困难是产生s1所有字符的全排列
# 根据组合数学的结论，如果n个字符进行全排列，其可能的字符串的个数位n! (n的阶乘)
# 如过是20个字符串，每微秒处理一个，需要近8万年的时间
# #暴力法恐怕不能算是个好算法


# 解法4：计数比较
# 解题思路：对比两个词中每个字母出现的次数，如果26个个字母出现的次数都相同的话，这两个字符串一定就是变位词
# 具体做法：为每个词设置一个26为的计数器，先检查每个词，在计数器中设定好每个字母出现的次数
# 次数完成后，进入比较阶段，看两个字符串的计数器是否相同，如果相同则输出是变位词的结论
# 为每个词做一个计数器

def anagramSolution03(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')   # ord用来返回一个字符的unicode编码的，编码是连续的，s[i]和a这个字符编码差pos=0，表示s[i]就是a
        c1[pos] = c1[pos] +1          # 那么s[i]这个字符的计数器的位置就是c1[pos],在c1列表的第一位，计数器+1，所以c1[pos]的值要加1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK: # 一共26个字母
        if c1[j] == c2[j]:
            j = j+1
        else:
            stillOK = False
    return stillOK

print(anagramSolution03('apple', 'pleap'))

# 算法分析
# 有3个循环迭代，但不存在嵌套循环
# 总操作次数T(n) = 2n+26,其数量级为O(n)
# 本算法依赖与两个长度为26的计数器列表，比前三个算法需要更多的存储空间，如果是中文，需要更多的存储空间
# 以空间换时间，时间和空间之间的取舍和权衡，在算法的选择和编程的设计经常存在。
# 可以把计数器改成字典的形式