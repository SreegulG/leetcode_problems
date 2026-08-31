class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        nxt = self.left.next

        self.left.next = new_node
        nxt.prev = new_node
        new_node.prev = self.left
        new_node.next = nxt

        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        prev_node = self.right.prev.prev
        curr = self.right.prev
        prev_node.next = self.right
        self.right.prev = prev_node
        curr.next = None
        curr.prev = None
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
