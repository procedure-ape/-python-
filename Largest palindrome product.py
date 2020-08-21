result = []
lists = []
for i in range(100,1000):
    for l in range(100,1000):
        data = i*l
        new = 0
        while data>0:
            new = new*10+data%10
            data = data//10
        data = i*l
        if data == new:
            result.append({data: "%s %s" %(i, l)})
            lists.append(data)
# print(result)
index = 0
while index != len(lists):
    if lists[index] < lists[index+1]:
        index = index + 1
    else:
        lists[index], lists[index+1] = lists[index+1], lists[index]
        index = index - 1

print(lists)