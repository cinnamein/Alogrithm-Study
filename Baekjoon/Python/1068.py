import sys

# 노드 수
n = int(sys.stdin.readline())
# 각 노드의 부모 노드
tmp = list(map(int, sys.stdin.readline().split()))
tree = dict(list())
for k in range(n):
    tree[k] = list()
# 노드 제거
num = int(sys.stdin.readline())
tree[num] = list()
root = 51
# {부모 노드 : [자식 노드]}
for i in range(n):
    if i == num:
        continue
    elif tmp[i] == -1:
        root = i
    else:
        tree[tmp[i]].append(i)
res = 0


def search(node):
    global res
    if node == num:
        return
    elif len(tree[node]) == 0:
        res += 1
        return
    while len(tree[node]) != 0:
        search(tree[node].pop())

if root == 51:
    print(0)
else:
    search(root)
    print(res)
