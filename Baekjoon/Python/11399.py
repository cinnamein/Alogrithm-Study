test = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
for i in range(test):
    result += arr[i] * (test - i)
print(result)
