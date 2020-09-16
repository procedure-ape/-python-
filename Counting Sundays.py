# 数星期日
# 下列信息是已知的，当然你也不妨自己再验证一下。

# 1900年1月1日是星期一。
# 三十天在九月中，
# 四六十一也相同。
# 剩下都是三十一，
# 除去二月不统一。
# 二十八天平常年，
# 多加一天在闰年。
# 闰年指的是能够被4整除却不能被100整除的年份，或者能够被400整除的年份。
# 在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是星期天？

import datetime

index = [1901, 1, 1]
result = []
while True:
  if datetime.datetime(index[0],index[1],index[2]).weekday() == 6:
    print(index)
  if index[0]==2000 and index[1]==1:
    break
  else:
    if index[1] == 12:
      index[0] += 1
      index[1] = 1
    else:
      index[1] += 1
