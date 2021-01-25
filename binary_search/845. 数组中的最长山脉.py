class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if not arr or len(arr) < 3:
            return 0
        n = len(arr)
        maxLen = 0
        left = 0
        while left + 2 < n:
            right = left + 1
            if arr[left] < arr[left + 1]:
                while right < n - 1  and arr[right] < arr[right + 1]:
                    right += 1
                if right < n - 1 and arr[right] > arr[right + 1]:
                    while right < n - 1 and arr[right] > arr[right + 1]:
                        right += 1
                    maxLen = max(maxLen, right - left + 1)
                else:
                    right += 1
            left = right
        return maxLen