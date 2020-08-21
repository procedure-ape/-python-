data = 600851475143
lists = []

for i in range(2, 10000000):
    if data%i == 0:
        lists.append(i)
        data = data//i

print(lists)