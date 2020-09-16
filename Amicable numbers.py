# 亲和数
# 记d(n)为n的所有真因数（小于n且整除n的正整数）之和。
# 如果d(a) = b且d(b) = a，且a ≠ b，那么a和b构成一个亲和数对，a和b被称为亲和数。

# 例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和110，因此d(220) = 284；而284的真因数包括1、2、4、71和142，因此d(284) = 220。

# 求所有小于10000的亲和数的和。

result = 0
for i in range(4,10001):
  b = 0
  a = 0
  for j in range(1,i//2+1):
    if i%j == 0:
      b += j
  for l in range(1,b//2+1):
    if b%l == 0:
      a += l
  if a == i and a != b:
    result += a

print(result)