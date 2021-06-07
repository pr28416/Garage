import warnings


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

    # def delete(self, val):
    #     # Check if BST is empty
    #     if self.length == 0:
    #         return None
    #     return self._delete(self.root, val)

    # def _delete(self, root, val): # Recursion
    #     if
    #
    #     prevNode = None
    #     travNode = self.root
    #     while not travNode.isLeaf():
    #         if val == travNode.val: # Check if val found
    #             pass
    #         elif val < travNode.val: # Check if go left
    #             pass
    #         else: # Go right
    #             pass

    def preOrderIterate(self):
        return self._preOrderIterate(self.root)

    def _preOrderIterate(self, travNode):
        if travNode is None: return
        yield travNode.val
        yield from self._preOrderIterate(travNode.left)
        # print(travNode.val)
        yield from self._preOrderIterate(travNode.right)

bst = BST()
for i in "PTERODACTYL":
    bst.insert(i)

print(list(bst.preOrderIterate()))