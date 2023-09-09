from collections import deque
import sys

deque = deque()
n = int(sys.stdin.readline())
output = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        num = int(command[1])
        deque.append(num)
    elif command[0] == "pop":
        if not deque:
            output.append(-1)
        else:
            output.append(deque.popleft())
    elif command[0] == "size":
        output.append(len(deque))
    elif command[0] == "empty":
        if not deque:
            output.append(1)
        else:
            output.append(0)
    elif command[0] == "front":
        if not deque:
            output.append(-1)
        else:
            output.append(deque[0])
    elif command[0] == "back":
        if not deque:
            output.append(-1)
        else:
            output.append(deque[-1])

for item in output:
    print(item)
