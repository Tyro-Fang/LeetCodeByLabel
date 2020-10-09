class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST( nums) :
        if not nums:
            return None
        return convert(nums, 0, len(nums) - 1)
        
def convert( nums, start, end):
    if start == end:
        return TreeNode(nums[start])
    mid = start + (end - start) // 2
    root = TreeNode(nums[mid])
    if mid -1 >= start:
        root.left = convert(nums, start, mid - 1)
    if mid + 1 <= end:
        root.right = convert(nums, mid + 1, end)
    return root

a=[-10,-3,0,5,9]
b=sortedArrayToBST(a)
print(b)