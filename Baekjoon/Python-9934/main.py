import sys

test = int(sys.stdin.readline())
result = [""] * (2 ** test - 1)

def order(num, length, count):
    global result
    if count == test:
        return
    tmp = (num + length) // 2
    result[count] = result[count] + str(arr[tmp]) + " "
    order(num, tmp - 1, count + 1)
    order(tmp + 1, length, count + 1)

arr = list(map(int, sys.stdin.readline().split()))
order(0, len(arr) - 1, 0)
for k in range(0, test):
    print(result[k])