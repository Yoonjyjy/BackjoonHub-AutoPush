while True:
    n = input()
    if n == "0":
        break

    is_p = True
    for i in range(len(n) // 2):
        if n[i] != n[-i-1]:
            is_p = False
            break

    print("yes") if is_p else print("no")