class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD,MUTIPLY, SUBTRACT, DIVISION = 0, 1, 2, 3
        def helper(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for operation in range(4):
                            if k < 2 and i > j:
                                continue
                            if operation == ADD:
                                newNums.append(x + y)
                            if operation == SUBTRACT:
                                newNums.append(x - y)
                            if operation == MUTIPLY:
                                newNums.append(x * y)
                            if operation == DIVISION:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if helper(newNums):
                                return True
                            newNums.pop()
            return False
        return helper(nums)

                    
        
        