#!/usr/bin/python
# python一行代码实现的功能

import sys

print('================python import mode================')

for i in sys.argv:
    print(i)

print('\n python 路径为',sys.path)

a = 'asd'
b = 'dsa'
# 一行代码交换a,b
a,b = b,a
print(a,b)

# 一行代码反转列表
c = [1,2,3][::-1]
print(c)

# 一行代码合并两个字典
d = {**{'a':1,'b':2}, **{'c':3}} 
print(d)

# 一行代码列表去重
e = set([1,2,3,2,3,7,9])
print(e)

# 一行代码求多个列表中的最大值
f = max(max([[1,2,3],[5,1],[4]], key=lambda v: max(v)))
print(f)

# 一行代码生成逆序序列
list(range(10, -1, -1))

# 绝对值或负数的模
In [1]: abs(-6)
Out[1]: 6