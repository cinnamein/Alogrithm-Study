n, m, v = map(int, input().split())
result = (v - n) / (n - m)
if result % 1 == 0:
    result += 1
else:
    result += 2
print(int(result))
