import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arrSet = sorted(list(set(arr)))
res = dict()
for i in range(len(arrSet)):
    res[arrSet[i]] = i
for k in arr:
    print(res[k], end=' ')
