class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        max_index = 0
        for i, v in enumerate(nums):
            if max_index >= len(nums) - 1:
                return True
            elif max_index >= i:
                max_index = max(max_index, i + v)
        return max_index >= len(nums) - 1
                

