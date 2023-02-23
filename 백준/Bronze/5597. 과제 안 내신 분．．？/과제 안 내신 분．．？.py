list = []
for i in range(28):
    list.append(int(input()))
num = 1

for i in range(30):
    if i + 1 not in list:
        print(i + 1)