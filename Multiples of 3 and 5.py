# 3的倍数和5的倍数
# 如果我们列出10以内所有3或5的倍数，我们将得到3、5、6和9，这些数的和是23。

# 求1000以内所有3或5的倍数的和。

data = []
for i in range(1,201):
    data.append(i * 5)

for i in range(1,334):
    if i%5 != 0:
        data.append(i*3)

print(data)