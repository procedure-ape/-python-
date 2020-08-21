lists = []
for i in range(10,1000000000):
    l = 1
    while l < 21:
        if i%l != 0:
            l = 25
        l = l + 1
    if l == 21:
        lists.append(i)

print(lists)