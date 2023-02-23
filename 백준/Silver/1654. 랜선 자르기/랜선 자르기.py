K, N = map(int, input().split())
lines = []
length = 1

for i in range(K):
    lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)