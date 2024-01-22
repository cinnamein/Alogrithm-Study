n, s = map(int, input().split())
li = list(map(int, input().split()))
result = 0
tmp = list()


def track(index):
    global result
    if sum(tmp) == s and len(tmp) > 0:
        result += 1
    for i in range(index, n):
        tmp.append(li[i])
        track(i + 1)
        tmp.pop()


track(0)
print(result)
