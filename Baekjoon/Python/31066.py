import sys

T = int(sys.stdin.readline())


def solution():
    N, M, K = map(int, input().split())
    result = 0

    a, b, c, d = N, M, 0, 0

    movement = M * K
    if N > movement and M == 1 and K == 1:
        return -1

    while a > 0:
        x = M * K
        a -= x
        c += x
        result += 1
        if a <= 0:
            break
        x = 1
        a += x
        c -= x
        result += 1
    return result


for _ in range(T):
    print(solution())
