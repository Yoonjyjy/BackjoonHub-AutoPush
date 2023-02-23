C = input()
res = 0.0

if C[0] == "A":
    res += 4
elif C[0] == "B":
    res += 3
elif C[0] == "C":
    res += 2
elif C[0] == "D":
    res += 1

if C[0] != "F":
    if C[1] == "+":
        res += 0.3
    elif C[1] == "-":
        res -= 0.3

print(res)