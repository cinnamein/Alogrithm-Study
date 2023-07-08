import itertools

n, m = map(int, input().split())

# def check(result, cnt, num):
#     result += str(num) + " "
#     cnt += 1
#     if m == cnt:
#         print(result)
#         return
#     for i in range(num, n - cnt + 2):
#         check(result, cnt, i)
#
# for k in range(1, n - m + 2):
#     check("", 0, k)

arr = list(range(1, n + 1))

list = itertools.permutations(arr, m)

for i in list:
    for ii in i:
        print(ii, end=" ")
    print()
