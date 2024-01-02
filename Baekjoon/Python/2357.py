import math
import sys


def init_segment(node, start, end):
    if start == end:
        segment[node] = (sequence[start], sequence[start])
        return segment[node]
    mid = (start + end) // 2
    left = init_segment(node * 2, start, mid)
    right = init_segment(node * 2 + 1, mid + 1, end)
    maxValue = max(left[0], right[0])
    minValue = min(left[1], right[1])
    segment[node] = (maxValue, minValue)
    return segment[node]


def search(node, start, end):
    if start > b or end < a:
        return (0, 1000000000)
    if start >= a and end <= b:
        return segment[node]
    mid = (start + end) // 2
    left = search(node * 2, start, mid)
    right = search(node * 2 + 1, mid + 1, end)
    maxValue = max(left[0], right[0])
    minValue = min(left[1], right[1])
    return (maxValue, minValue)


n, m = map(int, sys.stdin.readline().split())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
size = 1 << (math.ceil(math.log2(n)) + 1)
segment = [0 for _ in range(size)]
init_segment(1, 0, n - 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    result = search(1, 0, n - 1)
    print(result[1], result[0])
