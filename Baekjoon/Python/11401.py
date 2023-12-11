n, k = map(int, input().split())
p = 1000000007


def factorial(a):
    tmp = 1
    for i in range(2, a + 1):
        tmp = (tmp * i) % p
    return tmp


def square(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a

    tmp = square(a, b // 2)
    if b % 2:
        return tmp * tmp * a % p
    else:
        return tmp * tmp % p


numerator = factorial(n)
denominator = factorial(n - k) * factorial(k) % p

print(numerator * square(denominator, p - 2) % p)
