# 最大质因数
# 13195的所有质因数为5、7、13和29。

# 600851475143最大的质因数是多少？

data = 600851475143
lists = []

for i in range(2, 10000000):
    if data%i == 0:
        lists.append(i)
        data = data//i

print(lists)