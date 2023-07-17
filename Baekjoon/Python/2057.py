n = int(input())
arr = list()
arr[0] = 1
arr[1] = 1


def dp():
    


for i in range(2, n + 1):
    arr[i] = arr[i - 1] * i

for ii in range(n + 1):
    dp()
