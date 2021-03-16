"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        cur = root
        pre = None
        head = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre:
                pre = cur
                head = pre
            else:
                pre.right = cur
                cur.left = pre
                pre = cur
            cur = cur.right
        if pre:
            head.left = pre
            pre.right = head
        return head


#递归写法
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    pre = None
    head = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        global pre
        global head
        pre = None
        head = None
        self.dfs(root)
        if pre:
            head.left = pre
            pre.right = head
        return head
        

    def dfs(self, root):
        global pre
        global head
        if not root:
            return
        self.dfs(root.left)
        if not pre:
            pre = root
            head = pre
        else:
            pre.right = root
            root.left = pre
            pre = root
        self.dfs(root.right)
        

        