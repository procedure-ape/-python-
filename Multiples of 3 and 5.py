data = []
for i in range(1,201):
    data.append(i * 5)

for i in range(1,334):
    if i%5 != 0:
        data.append(i*3)

print(data)