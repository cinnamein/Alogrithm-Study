t = int(input())
arr0 = [0] * 41
arr1 = [0] * 41
arr0[0] = 1
arr0[1] = 0
arr1[0] = 0
arr1[1] = 1

for i in range(2, 41):
    arr0[i] = arr0[i - 1] + arr0[i - 2]
    arr1[i] = arr1[i - 1] + arr1[i - 2]

for _ in range(t):
    n = int(input())
    print(arr0[n], arr1[n])
