from collections import deque
n = int(input())
queue = deque([])

for _ in range(n):
    arr = input().split()
    if arr[0] == "push":
        queue.append(arr[1])
    elif arr[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            queue.popleft()
    elif arr[0] == "size":
        print(len(queue))
    elif arr[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif arr[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
