import heapq
import sys

# 병사의 수
n = int(sys.stdin.readline())
# 군번 순서대로 차출된 횟수
li = list(map(int, sys.stdin.readline().split()))
# 전화 문의 횟수
q = int(sys.stdin.readline())

for _ in range(q):
    cnt = []
    for i in range(n):
        # 횟수, 군번
        heapq.heappush(cnt, [li[i], i])

    # 식당 차출 프로그램 가동일수, 군번
    d, x = map(int, sys.stdin.readline().split())
    x -= 1

    if n == 3:
        # 병사가 3명일 경우 차출된 횟수 차이가 줄어들지 않음
        print(d)
    else:
        day = (30 * n - sum(li) + 2) // 3
        for i in range(day):
            # 반복문 1회 반복 시 하루가 지남
            currentDay = []
            for _ in range(3):
                # 3명 차출
                tmp = heapq.heappop(cnt)
                heapq.heappush(currentDay, [tmp[0] + 1, tmp[1]])
            for _ in range(3):
                heapq.heappush(cnt, heapq.heappop(currentDay))
            if i == d - 1:
                break
        # 차출 횟수가 동일해진 이후
        last = (day * 3 + sum(li)) % n
        for i in cnt:
            if i[1] == x:
                if last < x:
                    # 시뮬레이션이 끝나는 시점에서 마지막으로 차출된 병사보다 군번이 높을 경우
                    print(day * 3 // n - li[x])
                    print(222222)
                else:
                    # 시뮬레이션이 끝나는 시점에서 마지막으로 차출된 병사보다 군번이 낮거나 같은 경우
                    print(day * 3 // n - 1)
                    print(333333)
