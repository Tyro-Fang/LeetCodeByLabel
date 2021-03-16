class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        dicts = {}
        for val in nums:
            cur = [[val]]
            for key in dicts:
                if key <= val:
                    for prevResult in dicts[key]:
                        cur.append(prevResult + [val])
            dicts[val] = cur
        result = []
        for key in dicts:
            for prevResult in dicts[key]:
                if len(prevResult) > 1:
                    result.append(prevResult)
        return result