import sys

n = int(sys.stdin.readline())
res = []
if n == 1000:
    print(144)
elif n >= 100:
    for i in range(1, n + 1):
        arr = list(map(int, str(i)))
        for k in range(len(arr) - 2):
            if arr[k] - arr[k + 1] == arr[k + 1] - arr[k + 2]:
                res.append(i)
    print(len(res) + 99)
else:
    print(n)
