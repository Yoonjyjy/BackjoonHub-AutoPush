N = int(input())
isFind = False

for i in range(1, N + 1):
    sum = i
    num = i
    while num >= 10:
        sum += num % 10
        num //= 10
    sum += num

    if sum == N and isFind == False:
        print(i)
        isFind = True

if isFind == False:
    print(0)
