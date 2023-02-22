numbering = list(map(int, input().split()))
check = 0
for ch in numbering:
    check += (ch * ch)
check %= 10

print(check)