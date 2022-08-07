class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    values = []
    print(node.left)
    for value in vars(node).values():
        values.append(value)

    return values

print(tree_by_levels(Node(12,13,Node(14,15,None))))