# 偶斐波那契数
# 斐波那契数列中的每一项都是前两项的和。由1和2开始生成的斐波那契数列前10项为：

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 考虑该斐波那契数列中不超过四百万的项，求其中为偶数的项之和。

lists = [1, 2]
print(len(lists)-1)
while lists[len(lists)-1]<4000000:
    lists.append(lists[len(lists)-1]+lists[len(lists)-2])
print(lists)