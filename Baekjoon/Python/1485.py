import sys

t = int(sys.stdin.readline())
for _ in range(t):
    li = list()
    for i in range(4):
        li.append(list(map(int, sys.stdin.readline().split())))
    li.sort()
    flag = False
    # 대각선의 길이가 같은지 확인
    if (li[0][0] - li[3][0]) ** 2 + (li[0][1] - li[3][1]) ** 2 == (li[1][0] - li[2][0]) ** 2 + (li[1][1] - li[2][1]) ** 2:
        # 네 변의 길이가 같은지 확인
        a = (li[0][0] - li[1][0]) ** 2 + (li[0][1] - li[1][1]) ** 2
        b = (li[0][0] - li[2][0]) ** 2 + (li[0][1] - li[2][1]) ** 2
        c = (li[3][0] - li[1][0]) ** 2 + (li[3][1] - li[1][1]) ** 2
        d = (li[3][0] - li[2][0]) ** 2 + (li[3][1] - li[2][1]) ** 2
        if a == b == c == d:
            flag = True
    if flag:
        print(1)
    else:
        print(0)
