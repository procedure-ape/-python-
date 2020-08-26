# 最长考拉兹序列
# 在正整数集上定义如下的迭代序列：

# n → n/2 （若n为偶数）
# n → 3n + 1 （若n为奇数）
# 从小于一百万的哪个数开始，能够生成最长的序列呢？

def longest(data):
    lists = [data]
    while data != 1:
        if data % 2 == 0:
            data = data / 2
            lists.append(data)
        else:
            data = (data * 3) + 1
            lists.append(data)
    else:
        return lists

dataLen = 0
index = 0
for i in range(1,1000000):
    if len(longest(i)) > dataLen:
        dataLen = len(longest(i))
        index = i

print(index)