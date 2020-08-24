# 求第10001个素数

lists = [2]
for i in range(1,100000):
    data = i*2+1
    l = 0
    while l<len(lists):
        if data % lists[l] == 0:
            break
        l += 1
    else:
        lists.append(data)

print(lists[10001])