from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

    def hasLeft(self):
        return self.left is not None

    def hasRight(self):
        return self.right is not None

class BST:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, val): # Iteration
        # Increase length
        self.length += 1

        # Empty BST
        if self.length == 1:
            self.root = Node(val)
            return

        # Nonempty BST - need to traverse
        travNode = self.root
        while not travNode.isLeaf():
            if val < travNode.val: # Check against left
                if travNode.hasLeft(): # Can still go left
                    travNode = travNode.left
                else: # No left node
                    travNode.left = Node(val)
                    return
            else: # Go right otherwise
                if travNode.hasRight(): # Can still go right
                    travNode = travNode.right
                else: # No right node
                    travNode.right = Node(val)
                    return

        # Hit a leaf node without adding new val
        if val < travNode.val:
            travNode.left = Node(val)
        else:
            travNode.right = Node(val)

    def inorder(self):
        return self._iterate(self.root, "inorder")

    def preOrder(self):
        return self._iterate(self.root, "preorder")

    def postOrder(self):
        return self._iterate(self.root, "postorder")

    def levelOrder(self):
        queue = deque()
        queue.appendleft(self.root)
        while len(queue) > 0:
            trav = queue.pop()
            if trav == None: continue
            yield trav.val
            queue.appendleft(trav.left)
            queue.appendleft(trav.right)

    def _iterate(self, travNode, itype):
        if travNode is None: return
        if itype == "preorder": yield travNode.val
        yield from self._iterate(travNode.left, itype)
        if itype == "inorder": yield travNode.val
        yield from self._iterate(travNode.right, itype)
        if itype == "postorder": yield travNode.val

bst = BST()
for i in "PTERODACTYL":
    bst.insert(i)

print(list(bst.preOrder()))
print(list(bst.inorder()))
print(list(bst.postOrder()))
print(list(bst.levelOrder()))