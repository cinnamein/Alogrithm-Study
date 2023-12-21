import sys

r, c = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().rstrip()) for _ in range(r))
alphabet = [False] * 26
movementX = [-1, 1, 0, 0]
movementY = [0, 0, -1, 1]
result = 0


def dp(x, y, cnt, al, st):
    global result
    result = max(result, cnt)
    if 0 <= x < c and 0 <= y < r:
        st += board[y][x] + ' '
        tmp = ord(board[y][x])
        if not al[tmp - 65]:
            al[tmp - 65] = True
            cnt += 1
            for i in range(4):
                dp(x + movementX[i], y + movementY[i], cnt, al, st)
            al[tmp - 65] = False


dp(0, 0, 0, alphabet, '')
print(result)
