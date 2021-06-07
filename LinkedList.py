class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = Node(None)

    def _getNode(self, index):
        trav = self.head
        for _ in range(index+1):
            trav = trav.next
        return trav

    def get(self, index):
        if index < 0 or index >= self.length: return None
        return self._getNode(index).val

    def append(self, val):
        prevNode = self._getNode(self.length-1)
        prevNode.next = Node(val)
        self.length += 1

    def insert(self, index, val):
        if index < 0: return
        if index >= self.length:
            self.append(val)
            return
        prevNode = self._getNode(index-1)
        newNode = Node(val)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        prevNode = self._getNode(index-1)
        removed = prevNode.next
        prevNode.next = prevNode.next.next
        self.length -= 1
        return removed

    def iter(self):
        trav = self.head
        for _ in range(self.length):
            trav = trav.next
            yield trav.val

lst = LinkedList()
print(" ".join(map(str, lst.iter())))
lst.append(1)
print(" ".join(map(str, lst.iter())))
lst.append(3)
print(" ".join(map(str, lst.iter())))
lst.append(5)
print(" ".join(map(str, lst.iter())))
lst.insert(2, 4)
print(" ".join(map(str, lst.iter())))
print("got", lst.get(0))
print("got", lst.get(1))
print("got", lst.get(2))
print("got", lst.get(3))
print("got", lst.get(4))
print("removed idx 1:", lst.remove(1).val)
print(" ".join(map(str, lst.iter())))
print("removed idx 0:", lst.remove(0).val)
print(" ".join(map(str, lst.iter())))
