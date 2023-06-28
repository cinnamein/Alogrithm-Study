import sys

def track(sum, num):
    sum = sum + num + " "
    for k in range(len(tmp)):


while True:
    global tmp
    tmp = map(int, sys.stdin.readline().split())
    if tmp[0] == 0:
        break
    global sum
    sum = ""
    for i in range(len(tmp)):
        track(sum, i)
