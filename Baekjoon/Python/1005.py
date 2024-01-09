from collections import deque


def calc_topological_sort(time, matrix, link):
    result = [0] * (len(link) + 1)
    queue = deque()

    for i in range(1, len(link)):
        if link[i] == 0:
            result[i] = time[i]
            queue.append(i)

    while queue:
        prev = queue.popleft()

        for i in range(1, len(link)):
            if matrix[prev][i]:
                result[i] = max(result[i], result[prev] + time[i])
                link[i] -= 1

                if link[i] == 0:
                    queue.append(i)

    return result


def main():
    test_cases = int(input())
    result_str = ""

    for _ in range(test_cases):
        N, K = map(int, input().split())
        time = [0] + list(map(int, input().split()))
        matrix = [[False] * (N + 1) for _ in range(N + 1)]
        link = [0] * (N + 1)

        for _ in range(K):
            X, Y = map(int, input().split())
            matrix[X][Y] = True
            link[Y] += 1

        W = int(input())
        result = calc_topological_sort(time, matrix, link)[W]
        result_str += f"{result}\n"

    print(result_str)


if __name__ == "__main__":
    main()
