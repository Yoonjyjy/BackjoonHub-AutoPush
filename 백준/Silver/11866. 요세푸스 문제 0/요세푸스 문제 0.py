from collections import deque

N, K = map(int, input().split())
q = deque([i+1 for i in range(N)])
result = []

while q:
    q.rotate(-K+1)  # deque를 회전시킴
    result.append(str(q.popleft()))

print("<" + ", ".join(result) + ">")
