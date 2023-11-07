import sys


def mode_check(s):
    uppCnt = 0
    underbarCnt = 0
    tmp = 0

    if len(s) > 0 and s[0].isupper():
        return 'ERROR'

    if len(s) > 0 and s[0] == '_':
        return 'ERROR'

    if len(s) > 0 and s[-1] == '_':
        return 'ERROR'

    for c in s:
        if c.isupper():
            uppCnt += 1
            tmp = 0
        elif c == '_':
            underbarCnt += 1
            tmp += 1
            if tmp == 2:
                return 'ERROR'
        else:
            tmp = 0

    if uppCnt != 0 and underbarCnt != 0:
        return 'ERROR'

    if underbarCnt > 0:
        return 'C'
    else:
        return 'JAVA'


def convert_java_to_cpp(s):
    cv = ''
    for c in s:
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            cv += '_'
            cv += c.lower()
        else:
            cv += c

    return cv


def convert_cpp_to_java(s):
    cv = ''
    upper_flg = False
    for c in s:
        if c == '_':
            upper_flg = True
        else:
            if upper_flg:
                cv += c.upper()
                upper_flg = False
            else:
                cv += c

    return cv


variable_name = sys.stdin.readline().rstrip()
mode = mode_check(variable_name)

if mode == 'JAVA':
    print(convert_java_to_cpp(variable_name))
elif mode == 'C':
    print(convert_cpp_to_java(variable_name))
else:
    print('Error!')
