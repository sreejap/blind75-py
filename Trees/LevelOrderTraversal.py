from collections import deque # this import is required
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    res = []
    q = []
    def bfs(node):
        while len(q)!=0:
            levelQ = []
            for i in range (len(q)):
                levelNode = q.popleft() # this is how we pop from the q 
                levelQ.append(levelNode.val)
                if levelNode.left:
                    q.append(levelNode.left)
    
                if levelNode.right:
                    q.append(levelNode.right)
            res.append(levelQ)        

    if root:
        q = deque([root]) # this is the correct way
        bfs (root)
    return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))
