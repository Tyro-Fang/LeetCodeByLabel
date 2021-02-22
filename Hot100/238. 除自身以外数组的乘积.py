class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        LeftList, RightList = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            LeftList[i] = LeftList[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            RightList[i] = RightList[i + 1] * nums[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(LeftList[i] * RightList[i])
        return res

