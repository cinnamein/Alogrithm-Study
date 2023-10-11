import sys
from queue import PriorityQueue

# 병사의 수
n = int(sys.stdin.readline())
# 군번 순서대로 차출된 횟수
li = list(map(int, sys.stdin.readline().split()))
# 전화 문의 횟수
q = int(sys.stdin.readline())
for _ in range(q):
    cnt = PriorityQueue()
    for i in range(n):
        # 횟수, 군번
        cnt.put([li[i], i])
    # 식당 차출 프로그램 가동일수, 군번
    d, x = map(int, sys.stdin.readline().split())
    x -= 1
    for _ in range(d):
        temp = PriorityQueue()
        for _ in range(3):
            tmp = cnt.get()
            temp.put([tmp[0] + 1, tmp[1]])
        for _ in range(3):
            cnt.put(temp.get())
    for i in range(n):
        tmp = cnt.get()
        if tmp[1] == x:
            print(tmp[0] - li[x])
