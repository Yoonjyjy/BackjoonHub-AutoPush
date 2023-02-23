N = int(input())
dic = set()
for i in range(N):
    dic.add(input().strip())

dic = list(dic)
dic.sort(key=lambda x: (len(x), x))

for word in dic:
    print(word)