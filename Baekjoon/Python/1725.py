import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.append(0)
stack = [[0, arr[0]]]
res = 0

if n == 1:
    print(arr[0])
else:
    for i in range(1, n + 1):
        cursor = i
        while stack and stack[-1][1] > arr[i]:
            cursor, tmp = stack.pop()
            res = max(res, tmp * (i - cursor))
        stack.append([cursor, arr[i]])
    print(res)
