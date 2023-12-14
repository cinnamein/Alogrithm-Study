def fibonacci(num):
    if num in fib:
        return fib[num]
    elif num % 2 == 0:
        res = (fibonacci(num // 2) * (fibonacci(num // 2 + 1) + fibonacci(num // 2 - 1))) % 1000000007
    else:
        res = (fibonacci((num + 1) // 2) ** 2 + (fibonacci((num - 1) // 2)) ** 2) % 1000000007
    fib[num] = res
    return res


n = int(input())
fib = {}
fib[0] = 0
fib[1] = 1
fib[2] = 1
print(fibonacci(n))
