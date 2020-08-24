# 求所有小于两百万的素数的和。（windows上跑炸了）

lists = [2]
for i in range(1,100000):
    index = i*2+1
    for l in lists:
        if index % l != 0:
            lists.append(i)

print(lists)