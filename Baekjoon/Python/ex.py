n = int(input())
li = [0, 1, 2, 3, 7, 2, 8]
if n < 6:
    print(li[n])
else:
    if n % 2 == 1:
        if n % 4 == 1:
            print(n - 3 + li[2])
        else:
            print(n - 3 + li[3])
    else:
        tmp = n // 4 * n - (2 * (n // 4 - 1)) - 2
        print(tmp)
        if n % 4 == 0:
            print(tmp + li[3])
        else:
            print(tmp + li[2])