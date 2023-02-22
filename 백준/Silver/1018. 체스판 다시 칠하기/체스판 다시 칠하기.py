# 보드 크기 정의
N, M = map(int, input().split())

# 보드 내용 정의
board = []
for i in range(N):
    board.append(list(map(lambda x: 1 if x == 'B' else 0, input())))

min_changes = N * M

# 10x10 -> 3*3 = 체스판 8x8 크기로 자를 경우 9가지 경우의 수 생김
# 각 판마다 W가 먼저오는 경우와 B가 먼저 오는 경우를 나누어 다시 칠해야 하는 수를 체크
for i in range(N-7):
    for j in range(M-7):
        white_first_changes = 0
        black_first_changes = 0
        for n in range(8):
            for m in range(8):
                if (n % 2 == m % 2):
                    if (board[n+i][m+j] == 0):
                        black_first_changes += 1
                    else:
                        white_first_changes += 1
                else:
                    if (board[n+i][m+j] == 0):
                        white_first_changes += 1
                    else:
                        black_first_changes += 1
        min_changes = min(min_changes, white_first_changes, black_first_changes)

print(min_changes)