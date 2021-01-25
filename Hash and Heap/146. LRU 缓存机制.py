class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dicts = {}
        self.head = DoubleListNode(0, 0)
        self.tail = DoubleListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nums = 0

    def get(self, key: int) -> int:
        if key not in self.dicts:
            return -1
        else:
            self.freshKey(key)
            return self.dicts[key].val

    def put(self, key: int, value: int) -> None:
        node = DoubleListNode(value, key)
        if key in self.dicts:
            point = self.dicts[key]
            point.val = value
            self.freshKey(key)
        else:
            if self.nums == self.capacity:
                self.dicts.pop(self.head.next.key)
                self.removeNode(self.head.next)
                self.nums -= 1
            self.addToTail(node)
            self.dicts[key] = node
            self.nums += 1

    def freshKey(self, key):
        point = self.dicts[key]
        self.removeNode(point)
        self.addToTail(point)

    def removeNode(self, point):
        point.prev.next = point.next
        point.next.prev = point.prev
    
    def addToTail(self, point):
        point.prev = self.tail.prev
        point.next = self.tail
        self.tail.prev.next = point
        self.tail.prev = point

    

class DoubleListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


a = LRUCache(3)
a.put(1, 1)
a.put(2, 2)
a.put(3, 3)
a.put(4, 4)
print(a.get(4))
print(a.get(3))
print(a.get(2))
print(a.get(1))
a.put(5, 5)
print(a.get(1))
print(a.get(2))
print(a.get(3))
print(a.get(4))
print(a.get(5))

