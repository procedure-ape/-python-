# 阶乘数字和
# n! 的意思是 n × (n − 1) × … × 3 × 2 × 1

# 例如，10! = 10 × 9 × … × 3 × 2 × 1 = 3628800，所以10!的各位数字和是 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27。

# 求出100!的各位数字和。

index = 1
for i in range(1,101):
  index = index*i
indexStr = str(index)
index = 0
for i in range(0,len(indexStr)):
  index += int(indexStr[i])

print(index)