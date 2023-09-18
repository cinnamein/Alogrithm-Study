import sys

n = int(sys.stdin.readline().strip())
count = 0
flag = True
word_set = set()

for i in range(n):
    word = sys.stdin.readline().strip()
    word_set.add(word[0])

    for j in range(1, len(word)):
        if word[j] != word[j - 1]:
            if word[j] in word_set:
                flag = False
                break
            word_set.add(word[j])

    if flag:
        count += 1
    flag = True
    word_set.clear()

print(count)
