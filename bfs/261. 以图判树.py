class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if len(edges) != n - 1:
            return False
        queue = [0]
        nodes = {0}
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in nodes:
                    queue.append(neighbor)
                    nodes.add(neighbor)
        return len(nodes) == n
        

    


    