N = int(input())
list = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if v == list[i]:
        cnt += 1

print(cnt)