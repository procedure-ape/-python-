# 幂的数字和
# 215 = 32768，而32768的各位数字之和是 3 + 2 + 7 + 6 + 8 = 26。
# 21000的各位数字之和是多少？

data = 2**1000
index = 0
lists = []

while data > 1:
  lists.append(int(data % 10))
  data = data/10
  index += int(data % 10)

print(index)