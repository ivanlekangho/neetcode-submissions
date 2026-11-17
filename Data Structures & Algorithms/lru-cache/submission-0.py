class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert_at_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        self._remove(node)
        self._insert_at_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self._remove(self.cache[key])
            self._insert_at_tail(self.cache[key])
        else:
            if (len(self.cache) >= self.capacity):
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self._insert_at_tail(new_node)
            self.cache[key] = new_node

        
