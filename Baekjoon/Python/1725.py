import sys

n = int(sys.stdin.readline())
if n == 1:
    print(sys.stdin.readline())
else:
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    res = 0
    for i in range(n):
        height = i
        while stack and stack[-1][1] >= arr[i]:
            height = stack[-1][0]
            width = i - height
            res = max(res, width * stack[-1][1])
            stack.pop()
        stack.append((height, arr[i]))
    print(res)

