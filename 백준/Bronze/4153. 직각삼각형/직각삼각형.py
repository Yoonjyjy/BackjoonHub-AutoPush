while True:
    tri = list(map(int, input().split()))
    if (tri[0] == 0 and tri[1] == 0 and tri[2] == 0):
        break

    MAX, other = 0, 0
    MAX = max(tri)

    for i in tri:
        if i == MAX:
            MAX = i * i
        else:
            other += i * i
    if MAX == other:
        print("right")
    else:
        print("wrong")
