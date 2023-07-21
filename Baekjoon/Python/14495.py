n = int(input())

arr = [1] * (n + 1)

for i in range(4, n + 1):
    arr[i] = arr[i] = arr[i - 1] + arr[i - 3]

print(arr[n])
