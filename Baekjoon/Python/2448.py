n = int(input())
result = [[" "] * (n // 3 * 5)] * n


for i in range(n, 0, -3):
    for ii in range(i // 3):
        print("*****", end = "")
        print()
        print(" * * ", end = "")
        print()
        print("  *  ", end = "")
        print()
