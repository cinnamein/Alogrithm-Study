n = int(input())
heap = [0, 1]

for i in range(2, n + 1):
    heap.append(i)
    tmpI = heap[i]
    heap[i] = heap[i - 1]
    heap[i - 1] = tmpI
    maximum = i - 1
    while maximum != 1:
        tmp = heap[maximum]
        heap[maximum] = heap[maximum // 2]
        heap[maximum // 2] = tmp
        maximum = maximum // 2
for i in range(1, n+1):
    print(heap[i], end=' ')
