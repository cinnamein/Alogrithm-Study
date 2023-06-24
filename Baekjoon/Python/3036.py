import sys


def gcd(a, b):
    num = 2
    while True:
        if num > a or num > b:
            break
        if a % num == 0 and b % num == 0:
            a = a / num
            b = b / num
            num = 2
        else:
            num = num + 1
    print(str(int(a)) + "/" + str(int(b)))


test = int(sys.stdin.readline())
tmp = sys.stdin.readline().split()
a = int(tmp[0])
for i in range(1, test):
    b = int(tmp[i])
    if a == b:
        print("1/1")
    else:
        gcd(a, b)
