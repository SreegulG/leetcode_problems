class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.next, node.prev = self.right, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next = node.prev = None

    def get(self, key: int) -> int:
        if key in self.cache:
            get_node = self.cache[key]
            self.remove(get_node)
            self.insert(get_node)
            return get_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
