import sys


def init_tree(node, start, end):
    if start == end:
        segment[node] = [sequence[start], start]
        return segment[node]
    mid = (start + end) // 2
    segment[node] = min(init_tree(node * 2, start, mid), init_tree(node * 2 + 1, mid, end))
    return segment[node]


def search(node, start, end):
    if start >= b and end <= c:
        return node
    mid = (start + end) // 2
    return min(search(node * 2, start, mid), search(node * 2 + 1, mid, end))


segment = [list()] * 4000000
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
init_tree(1, 0, n - 1)
m = int(sys.stdin.readline())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    print(segment)
    # if a == 1:
    # elif b == 2:
