import math
import sys

n = int(sys.stdin.readline())
s, m, l, xl, xxl, xxxl = map(int, sys.stdin.readline().split())
t, p = map(int, sys.stdin.readline().split())
print(math.ceil(s / t) + math.ceil(m / t) + math.ceil(l / t) + math.ceil(xl / t) + math.ceil(xxl / t) + math.ceil(xxxl / t))
print(n // p, n % p)
