import sys

li = [0, 1]
n = int(sys.stdin.readline())
for i in range(2, n % 1500000 + 1):
    li.append((li[i - 1] + li[i - 2]) % 1000000)
print(li[n % 1500000])
