import json

def serialize(root):
    def recur(node):
        return [node.val, recur(node.left), recur(node.right)] if node else None
    return json.dumps(recur(root))

def deserialize(data):
    def recur(data):
        if data is None:
            return None
        node = TreeNode(data[0])
        node.left = recur(data[1])
        node.right = recur(data[2])
        return node
    return recur(json.loads(data))
