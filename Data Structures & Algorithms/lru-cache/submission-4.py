class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
        else:
            if self.capacity <= len(self.cache):
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
                
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            




# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.cap = capacity
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
    
#     def insert(self, node):
#         ex_first = self.head.next
#         ex_first.prev = node
#         node.prev = self.head
#         node.next = ex_first
#         self.head.next = node
    
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]
#             self.remove(node)
#             self.insert(node)
#             return node.val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             self.remove(node)
#             node.val = value
#             self.insert(node)
#         else:
#             if len(self.cache) >= self.cap:
#                 lru_node = self.tail.prev
#                 self.remove(lru_node)
#                 del self.cache[lru_node.key]
            
#             self.cache[key] = Node(key, value)
#             self.insert(self.cache[key])
