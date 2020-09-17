# 姓名得分
# 在这个46K的文本文件names.txt（右击并选择“目标另存为……”）中包含了五千多个姓名。首先将它们按照字母序排列，然后计算出每个姓名的字母值，乘以它在按字母顺序排列后的位置，以计算出姓名得分。

# 例如，按照字母序排列后，位于第938位的姓名COLIN的字母值是3 + 15 + 12 + 9 + 14 = 53。因此，COLIN的姓名得分是938 × 53 = 49714。

# 文件中所有姓名的姓名得分之和是多少？

f = open('names.txt', 'r')
txt = f.read()
f.close()
txt = txt.split(',')
txt.sort()
index = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet.upper()
result = 0

for i in txt:
  index += 1
  i = list(i)
  names = 0
  for l in range(1,len(i)-1):
    names += (alphabet.find(i[l])+1)
  result += index*names

print(result)