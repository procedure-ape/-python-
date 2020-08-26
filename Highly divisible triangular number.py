# 高度可约的三角形数

index = 1
triangles = 0
lists = []
# index = 10000的时候都要跑很久，果然需要优化下吧
while index < 10000:
    triangles += index
    lists1 = []
    for i in range(1, int(triangles/2+1)):
        if triangles % i == 0:
            lists1.append(i)
    lists1.append(triangles)
    if len(lists1) > 500:
        print(triangles)
        print(lists1)
        break
    lists.append(lists1)
    index += 1
