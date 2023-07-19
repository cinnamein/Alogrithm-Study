n, m = map(int, input().split())
arr = [True] * (m - n + 1)

for i in range(2, int(m ** 0.5) + 1):
    tmp = i ** 2
    for ii in range(n // tmp * tmp, m + 1, tmp):
        if ii - n >= 0 and arr[ii - n]:
            arr[ii - n] = False

print(arr.count(True))
