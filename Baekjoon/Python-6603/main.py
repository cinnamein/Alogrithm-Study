def track(sum, num, cnt):
    cnt = cnt + 1
    sum = sum + str(tmp[num]) + " "
    if cnt == 6:
        print(sum)
        return
    for k in range(num + 1, len(tmp)):
        track(sum, k, cnt)


while True:
    global tmp, cnt, sum
    string = input()
    if string == "0":
         break
    tmp = list(map(int, string.split(" ")))
    sum = ""
    cnt = 0
    for i in range(1, len(tmp)):
        track(sum, i, cnt)
    print()
