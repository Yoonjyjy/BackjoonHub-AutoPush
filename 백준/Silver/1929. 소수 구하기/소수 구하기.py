import math

M, N = map(int, input().split())
list = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N) + 1)):
    if list[i]:
        for j in range(i * 2, N + 1, i):
            list[j] = False

for i in range(M, N+1):
    if list[i] and i != 1:
        print(i)