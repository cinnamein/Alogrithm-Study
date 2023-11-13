import sys

case = int(sys.stdin.readline())


def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for _ in range(case):
    n = int(sys.stdin.readline())
    if n == 0 or n == 1:
        print(2)
    else:
        while True:
            if check(n):
                print(n)
                break
            else:
                n += 1
