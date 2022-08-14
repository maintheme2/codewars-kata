class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
            
def tree_by_levels(node):
    if node == None:
        return []

    result, q = [], [node]

    while q:
        n = q.pop(0)

        if isinstance(n, Node):
            result.append(n.value)
            
            if n.left != None:
                q.append(n.left)

            if n.right != None:
                q.append(n.right)

    return result

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))