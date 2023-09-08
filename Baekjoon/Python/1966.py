from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    li = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while li:
        num = max(li)
        front = li.popleft()
        m -= 1

        if num == front:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            li.append(front)
            if m < 0:
                m = len(li) - 1
