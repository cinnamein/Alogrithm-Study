n = int(input())
result = 0
if n == 1 or n == 3:
    print(-1)
else:
    while n != 0:
        if n % 5 == 0:
            result += n / 5
            n = 0;
        else:
            n -= 2
            result += 1
    print(int(result))
