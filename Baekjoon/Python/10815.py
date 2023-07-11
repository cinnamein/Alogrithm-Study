def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 입력 받기
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 숫자 카드 정렬
cards.sort()

# 이진 탐색을 사용하여 숫자 카드 존재 여부 판단
result = []
for target in targets:
    if binary_search(cards, target):
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(' '.join(map(str, result)))
