n, p, q = map(int, input().split())
dic = {0: 1}


def dp(num):
    if num in dic:
        return dic[num]
    else:
        dic[num] = dp(num // p) + dp(num // q)
        return dic[num]


if n == 0:
    print(1)
else:
    print(dp(n // p) + dp(n // q))
