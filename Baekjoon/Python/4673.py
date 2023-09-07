num = [False] * 10001

for i in range(1, 10):
    num[i * 2] = True

for i in range(10, 100):
    num[i // 10 * 11 + i % 10 * 2] = True

for i in range(100, 1000):
    a = i // 100
    b = (i % 100) // 10
    num[a * 101 + b * 11 + i % 10 * 2] = True

for i in range(1000, 9973):
    a = i // 1000
    b = (i % 1000) // 100
    c = (i % 100) // 10
    try:
        num[a * 1001 + b * 101 + c * 11 + i % 10 * 2] = True
    except IndexError:
        pass

for k in range(1, 10001):
    if not num[k]:
        print(k)
