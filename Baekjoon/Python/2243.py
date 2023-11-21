import sys

n = int(sys.stdin.readline())
candy = [0] * 4000000


def put(taste, num, node, start, end):
    candy[node] += num
    if start == end:
        return
    mid = (start + end) // 2
    if taste <= mid:
        put(taste, num, node * 2, start, mid)
    else:
        put(taste, num, node * 2 + 1, mid + 1, end)


def take(rank, node, start, end):
    candy[node] -= 1
    if start == end:
        return start
    mid = (start + end) // 2
    if candy[node * 2] >= rank:
        return take(rank, node * 2, start, mid)
    else:
        return take(rank - candy[node * 2], node * 2 + 1, mid + 1, end)


for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        print(take(tmp[1], 1, 1, 1000000))
    elif tmp[0] == 2:
        put(tmp[1], tmp[2], 1, 1, 1000000)
