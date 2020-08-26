# 网格路径
# 从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。

# 对于20×20方阵来说，这样的路径有多少条？

lists = []
def lattice(data):
    if data[len(data)-1]['x'] == 3 and data[len(data)-1]['y'] == 3:
        lists.append(data)
    else:
        if data[len(data)-1]['x'] != 3:
            data.append({
                'x': data[len(data)-1]['x'] + 1,
                'y': data[len(data)-1]['y']
            })
            lattice(data)

        if data[len(data)-1]['y'] != 3:
            data.append({
                'x': data[len(data)-1]['x'],
                'y': data[len(data)-1]['y'] + 1
            })
            lattice(data)

lattice([{'x':0, 'y':0}])
print(lists)