import sys

while True:
    tmp = sys.stdin.readline()
    if tmp == '.\n':
        break
    arr = list(tmp)
    qu = []
    for i in arr:
        try:
            if i == '[':
                qu.append('[')
            elif i == ']':
                if qu.pop() == '[':
                    continue
                else:
                    print('no')
                    break
            elif i == '(':
                qu.append('(')
            elif i == ')':
                if qu.pop() == '(':
                    continue
                else:
                    print('no')
                    break
            elif i == '\n':
                if len(qu) == 0:
                    print('yes')
                else:
                    print('no')
        except:
            print('no')
            break
