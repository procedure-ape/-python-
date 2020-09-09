# 表达数字的英文字母计数
# 如果把1到5写成英文单词，分别是：one, two, three, four, five，这些单词一共用了3 + 3 + 5 + 4 + 4 = 19个字母。

# 如果把1到1000都写成英文单词，一共要用多少个字母？

# 注意： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含23个字母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式英语的规则。

_known = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

index = 0

for i in range(1,1000):
  data = ''
  if i > 99:
    data = data + _known[int(i/100)] + 'hundred'
    i = int(i%100)
    if i > 0:
      data += 'and'
  if i > 20:
    data = data + _known[int(i/10)*10]
    if i%10 > 0:
      data += _known[i%10]
  else:
    data = data + _known[i]
  index += len(data)
  index += len('Onethousand')

print(index)