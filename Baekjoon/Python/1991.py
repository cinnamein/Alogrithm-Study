import sys

n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    a, b, c = map(str, sys.stdin.readline().rstrip().split())
    tree[a] = [b, c]


def preorder(root):
    if root == '.':
        return
    tmp = tree[root][0]
    print(root, end='')
    preorder(tmp)
    preorder(tree[root][1])


def inorder(root):
    if root == '.':
        return
    tmp = tree[root][0]
    inorder(tmp)
    print(root, end='')
    inorder(tree[root][1])


def postorder(root):
    if root == '.':
        return
    tmp = tree[root][0]
    postorder(tmp)
    postorder(tree[root][1])
    print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
