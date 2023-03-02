def fact(n):
    res = 1
    while n >= 2:
        res *= n
        n -= 1
    return res


N, K = map(int, input().split())
print(int(fact(N) / (fact(K)*fact(N - K))))