test = int(input())
arr = [[0] * 2 for _ in range(test)]

for i in range(test):
    tmp = list(map(str, input().split()))
    arr[i][0] = int(tmp[0])
    arr[i][1] = tmp[1]

arr.sort(key=lambda x: x[0])

for k in range(test):
    print(arr[k][0], arr[k][1])
