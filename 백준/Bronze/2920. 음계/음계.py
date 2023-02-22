seq = list(map(int, input().split()))

if (seq == sorted(seq)):
    print("ascending")
elif (seq == sorted(seq, reverse=True)):
    print("descending")
else:
    print("mixed")
