class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return nums
        res = []
        left = right = 0
        queue = []
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop(-1)
            queue.append(nums[i])
            if right - left < k - 1:
                right += 1
            else:
                res.append(queue[0])
                if queue[0] == nums[left]:
                    queue.pop(0)
                left += 1
                right += 1
        return res
        
