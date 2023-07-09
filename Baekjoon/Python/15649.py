import itertools

n, m = map(int, input().split())

arr = list(range(1, n + 1))

list = itertools.permutations(arr, m)

for i in list:
    for ii in i:
        print(ii, end=" ")
    print()
