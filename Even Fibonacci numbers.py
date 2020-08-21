lists = [1, 2]
print(len(lists)-1)
while lists[len(lists)-1]<4000000:
    lists.append(lists[len(lists)-1]+lists[len(lists)-2])
print(lists)