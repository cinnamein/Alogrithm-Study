import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arrSum = [0] * (n * 4)


def init(start, end, index):
    if start == end:
        arrSum[index] = arr[start - 1]
        return arrSum[index]
    mid = (start + end) // 2
    arrSum[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return arrSum[index]


def search(start, end, index, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return arrSum[index]
    mid = (start + end) // 2
    return search(start, mid, index * 2, left, right) + search(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, updateIdx, updateData):
    if updateIdx < start or updateIdx > end:
        return
    arrSum[index] += updateData
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, updateIdx, updateData)
    update(mid + 1, end, index * 2 + 1, updateIdx, updateData)


init(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        tmp = c - arr[b - 1]
        arr[b - 1] = c
        update(1, n, 1, b, tmp)
    elif a == 2:
        print(search(1, n, 1, b, c))
