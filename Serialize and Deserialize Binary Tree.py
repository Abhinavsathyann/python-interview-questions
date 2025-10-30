from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return ""
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("#")  # Placeholder for None
    return ",".join(result)

def deserialize(data):
    if not data:
        return None
    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if values[i] != "#":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        if values[i] != "#":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root
