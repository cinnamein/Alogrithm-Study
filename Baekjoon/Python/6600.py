while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        # d: 행렬식
        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        # a: 원의 중심의 x값 좌표, b: 원의 중심의 y값 좌표
        a = ((x1 ** 2 + y1 ** 2) * (y2 - y3) + (x2 ** 2 + y2 ** 2) * (y3 - y1) + (x3 ** 2 + y3 ** 2) * (y1 - y2)) / d
        b = ((x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3) + (x3 ** 2 + y3 ** 2) * (x2 - x1)) / d
        result = ((a - x1) ** 2 + (b - y1) ** 2) ** 0.5 * 2 * 3.141592653589793
        print(round(result, 2))
    except EOFError:
        break
