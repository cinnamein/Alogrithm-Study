import itertools

n, m = map(int, input().split())

arr = list(range(1, n + 1))

result = itertools.combinations(arr, m)

for i in result:
    for ii in i:
        print(ii, end=" ")
    print()