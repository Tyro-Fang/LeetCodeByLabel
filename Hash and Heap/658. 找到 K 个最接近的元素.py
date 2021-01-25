#1.直接搜索k的范围
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if not arr or k == None or x ==None:
#             return []
#         arrLen = len(arr)
#         if arrLen <= k:
#             return arr
#         closedIndex = 0
#         if x <= arr[0]:
#             return arr[: k]
#         elif x >= arr[-1]:
#             return arr[arrLen - k:]
#         else:
#             left = 0
#             right = arrLen - k
#             while left < right:
#                 mid = (left + right) // 2
#                 if x - arr[mid] > arr[mid + k] - x:
#                     left = mid + 1
#                 else:
#                     right = mid
#             return arr[left: left + k]


#2.先找到最近的数，再搜索范围

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or k == None or x ==None:
            return []
        arrLen = len(arr)
        if arrLen <= k:
            return arr
        closedIndex = 0
        if x <= arr[0]:
            return arr[: k]
        elif x >= arr[-1]:
            return arr[arrLen - k:]
        else:
            left = 0
            right = arrLen - 1
            while left < right:
                mid = left + (right - left) // 2
                if x > arr[mid]:
                    left = mid + 1
                else:
                    right = mid 
            low = high = left
            while high - low < k + 1:
                if high > arrLen - 1:
                    low -= 1
                    continue
                if low < 0:
                    high += 1
                    continue
                if abs(x - arr[low]) > abs(arr[high] - x):
                    high += 1
                else:
                    low -= 1
            return arr[low + 1:high]


a=[0,0,1,2,3,3,4,7,7,8]
x=5
k=3
s = Solution()
s.findClosestElements(a,k,x)






