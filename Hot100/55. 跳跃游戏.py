class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        i = 0
        while i < len(nums) - 1:
            maxStep = 0
            maxIndex = 0
            if nums[i] == 0:
                return False
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] >= len(nums) - 1:
                    return True
                elif j + nums[j] > maxStep:
                    maxStep = j + nums[j]
                    maxIndex = j
                else:
                    continue
            i = maxIndex
        if i >= len(nums) - 1:
            return True
        return False
                

