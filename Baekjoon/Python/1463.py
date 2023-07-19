n = int(input())

num = [0] * 1000001
num[1] = 0
num[2] = 1
num[3] = 1

if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    for i in range(4, n + 1):
        num[i] = num[i - 1] + 1
        if i % 3 == 0:
            num[i] = min(num[i // 3] + 1, num[i])
        if i % 2 == 0:
            num[i] = min(num[i // 2] + 1, num[i])
    print(num[n])
