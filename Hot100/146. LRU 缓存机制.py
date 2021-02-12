class DoubleLinkedNode:
    def __init__(self, key, val):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dicts = {}
        self.firstNode = DoubleLinkedNode(0, 0)
        self.lastNode = DoubleLinkedNode(0, 0)
        self.firstNode.next = self.lastNode
        self.lastNode.prev = self.firstNode
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.dicts:
            self.refreshKey(key)
            return self.dicts[key].val
        else:
            return -1

    def refreshKey(self, key):
        node = self.dicts[key]
        self.remove(node)
        self.addToHead(node)
        
    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev

    def addToHead(self, node):
        firstNode = self.firstNode.next
        self.firstNode.next = node
        node.prev = self.firstNode
        node.next = firstNode
        firstNode.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.dicts:
            self.dicts[key].val = value
            self.refreshKey(key)
        else:
            if self.length == self.capacity:
                del self.dicts[self.lastNode.prev.key]
                self.remove(self.lastNode.prev)
                self.length -= 1
            node = DoubleLinkedNode(key, value)
            self.addToHead(node)
            self.dicts[key] = node
            self.length += 1





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)