sum = 0
count = 0

for _ in range(20):
    a, b, c = input().split()
    if c == "A+":
        sum += float(b) * 4.5
        count += float(b)
    elif c == "A0":
        sum += float(b) * 4.0
        count += float(b)
    elif c == "B+":
        sum += float(b) * 3.5
        count += float(b)
    elif c == "B0":
        sum += float(b) * 3.0
        count += float(b)
    elif c == "C+":
        sum += float(b) * 2.5
        count += float(b)
    elif c == "C0":
        sum += float(b) * 2.0
        count += float(b)
    elif c == "D+":
        sum += float(b) * 1.5
        count += float(b)
    elif c == "D0":
        sum += float(b)
        count += float(b)
    elif c == "F":
        count += float(b)
print(sum / count)