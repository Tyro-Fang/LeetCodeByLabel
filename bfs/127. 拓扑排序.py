"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        if not graph:
            return []
        queue = [graph[0]]
        nodes = {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = 1
                else:
                    nodes[neighbor] += 1
        queue = []
        res = []
        for node in graph:
            if node not in nodes:
                queue.append(node)
                res.append(node)
        
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                nodes[neighbor] -= 1
                if nodes[neighbor] == 0:
                    queue.append(neighbor)
                    res.append(neighbor)
                
        return res
            
 