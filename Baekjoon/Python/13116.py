import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    listA = []
    listB = []

    while a != 1:
        listA.append(a)
        a //= 2
    listA.append(1)

    while b != 1:
        listB.append(b)
        b //= 2
    listB.append(1)

    breaker = True
    while breaker:
        for k in range(len(listA)):
            for i in range(len(listB)):
                if listA[k] == listB[i]:
                    print(str(listA[k]) + "0")
                    breaker = False
                    break
            if not breaker:
                break