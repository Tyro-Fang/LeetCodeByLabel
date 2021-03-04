class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True
        #通过优化存储出点表可以减少一次for循环
        adj = [[] for _ in range(numCourses)]

        inQueue = [0] * numCourses
        nums = numCourses
        for val in prerequisites:
            inQueue[val[0]] += 1
            adj[val[1]].append(val[0])
        queue = []
        for i, v in enumerate(inQueue):
            if v == 0:
                queue.append(i)
        while queue:
            tempCourse = queue.pop(0)
            nums -= 1
            for val in adj[tempCourse]:
                inQueue[val] -= 1
                if inQueue[val] == 0:
                    queue.append(val)
                        
        return nums == 0

