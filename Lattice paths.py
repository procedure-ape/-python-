# 网格路径
# 从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。

# 对于20×20方阵来说，这样的路径有多少条？

def test(lists):
  newlist = []
  index = False
  for i in lists:
    if i['x'] != 20:
      newlist.append({'x': i['x']+1,'y': i['y']})
    if i['y'] != 20:
      newlist.append({'x': i['x'],'y': i['y']+1})
    if i['x'] == 20 and i['y'] == 20:
      index = True
  if index:
    print(len(lists))
  else:
    test(newlist)

test([{'x': 0,'y': 0}])