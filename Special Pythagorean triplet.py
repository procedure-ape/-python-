# 特殊毕达哥拉斯三元组
# 毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足a2 + b2 = c2,有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。

for A in range(1,332):
    for B in range(1,333):
        C = 1000 - A - B
        if A ** 2 + B ** 2 == C ** 2:
            print('%s %s %s'%(A,B,C))