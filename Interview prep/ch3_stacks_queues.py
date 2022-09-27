from inspect import ismemberdescriptor


class ListNode:
    def __init__(self, val=None, next=None): self.val, self.next = val, next
    def __repr__(self):return f'<ListNode v: {self.val}, hasNext: {self.next is not None}>'
    def __lt__(self, other): return self.val < other.val
    def __le__(self, other): return self.val <= other.val
    def __gt__(self, other): return self.val > other.val
    def __ge__(self, other): return self.val >= other.val


class ArrayStack:
    def __init__(self, *args): self.sk = list(args)

    def push(self, val): self.sk.append(val)

    def pop(self):
        if self.isEmpty(): raise(Exception("Cannot pop from empty stack"))
        return self.sk.pop()

    def peek(self):
        if self.isEmpty(): raise(Exception("Cannot peek from empty stack"))
        return self.sk[-1]

    def isEmpty(self): return len(self.sk) == 0

    def __len__(self): return len(self.sk)

    def __str__(self): return f'[{", ".join(list(map(str, self.sk[::-1])))}]'

class ListStack:
    def __init__(self, *args):
        self.head = None
        self.len = 0
        for i in args: self.push(i)
    
    def push(self, val):
        self.head = ListNode(val, self.head) if self.head else ListNode(val)
        self.len += 1
    
    def pop(self):
        if self.head is None: raise(Exception("Cannot pop from empty stack"))
        val = self.head.val
        self.head = self.head.next
        self.len -= 1
        return val

    def peek(self):
        if self.head is None: raise(Exception("Cannot peek from empty stack"))
        return self.head.val

    def isEmpty(self): return self.head is None

    def __len__(self): return self.len

    def __str__(self):
        trav = self.head
        arr = []
        while trav:
            arr.append(trav.val)
            trav = trav.next
        return f'[{", ".join(list(map(str, arr)))}]'

class ArrayQueue:
    def __init__(self, *args): self.qu = list(args)

    def append(self, val): self.qu.append(val)

    def remove(self):
        if self.isEmpty(): raise(Exception("Cannot remove from empty queue"))
        return self.qu.pop(0)
    
    def peek(self):
        if self.isEmpty(): raise(Exception("Cannot peek from empty queue"))
        return self.qu[0]

    def isEmpty(self): return len(self.qu) == 0

    def __str__(self): return f'[{", ".join(list(map(str, self.qu)))}]'

class ListQueue:
    def __init__(self, *args):
        self.head, self.tail = None, None
        for i in args: self.append(i)

    def append(self, val):
        if self.isEmpty(): self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def remove(self):
        if self.isEmpty(): raise(Exception("Cannot remove from empty queue"))
        val = self.head.val
        self.head = self.head.next
        if self.head is None: self.tail = None
        return val
    
    def peek(self):
        if self.isEmpty(): raise(Exception("Cannot peek from empty queue"))
        return self.head.val
    
    def isEmpty(self): return not(self.head or self.tail)

    def __str__(self):
        trav = self.head
        arr = []
        while trav:
            arr.append(trav.val)
            trav = trav.next
        return f'[{", ".join(list(map(str, arr)))}]'

class SetOfStacks():
    def __init__(self, capacity, *args):
        self.capacity = capacity
        self.supersk = []
        for i in args: self.push(i)

    def push(self, val):
        if self.isEmpty() or len(self.supersk[-1]) == self.capacity: self.supersk.append(ArrayStack())
        self.supersk[-1].push(val)

    def pop(self):
        if self.isEmpty(): raise(Exception("Cannot pop from empty stack"))
        return self.popAt(len(self.supersk)-1)

    def peek(self):
        if self.isEmpty(): raise(Exception("Cannot peek from empty stack"))
        return self.supersk[-1].peek()

    def popAt(self, index):
        if not(0 <= index < len(self.supersk)): raise(Exception("Attempted to pop from stack out of bounds"))
        val = self.supersk[index].pop()
        if self.supersk[index].isEmpty(): del self.supersk[index]
        return val
    
    def isEmpty(self):
        return len(self.supersk) == 0

    def __str__(self): return f'( {", ".join(list(map(str, self.supersk)))} )'

class StackQueue():
    def __init__(self, *args):
        self.mainSk, self.reserveSk, self.top = ArrayStack(), ArrayStack(), None
        for i in args: self.append(i)

    def append(self, val): self.reserveSk.push(val)

    def _refill(self, isRemoving):
        if self.mainSk.isEmpty():
            if self.reserveSk.isEmpty(): raise(Exception(f"Cannot {'remove' if isRemoving else 'peek'} from empty queue"))
            while not self.reserveSk.isEmpty():
                self.mainSk.push(self.reserveSk.pop())

    def remove(self):
        self._refill(True)
        return self.mainSk.pop()

    def peek(self):
        self._refill(True)
        return self.mainSk.peek()

    def isEmpty(self):
        return self.mainSk.isEmpty() and self.reserveSk.isEmpty()

    def __str__(self):
        return f'm:{str(self.mainSk)}, r:{str(self.reserveSk)}'

def sortStack(sk, skImplem=ArrayStack):
    tmpSk = skImplem()
    for n in range(len(sk), 0, -1):
        tmp = None
        for _ in range(n):
            v = sk.pop()
            if tmp is None or v < tmp: tmp = v
            tmpSk.push(v)
        for _ in range(n):
            v = tmpSk.pop()
            if v is not tmp: sk.push(v)
        tmpSk.push(tmp)
    while not tmpSk.isEmpty(): sk.push(tmpSk.pop())

# class AnimalShelter:
#     def __init__(self)

if __name__ == '__main__':
    # listSk = ListStack(1,2,3,4,5)
    # arrSk = ArrayStack(1,2,3,4,5)
    # print(listSk, arrSk)
    # listSk.push(6)
    # print(listSk)
    # print(listSk.pop())
    # print(listSk)
    # arrSk.push(6)
    # print(arrSk)
    # print(arrSk.pop())
    # print(arrSk)
    # listQu = ListQueue(1,2,3,4,5)
    # arrQu = ArrayQueue(1,2,3,4,5)
    # print(listQu, arrQu)
    # listQu.append(6)
    # print(listQu)
    # print(listQu.remove())
    # print(listQu)
    # arrQu.append(6)
    # print(arrQu)
    # print(arrQu.remove())
    # print(arrQu)
    # supersk = SetOfStacks(5, *[i for i in range(13)])
    # print(supersk)
    # print(supersk.pop(), supersk.pop(), supersk.pop(), supersk.pop())
    # print(supersk)
    # sq = StackQueue()
    # print(sq)
    # for i in range(8):
    #     print('added', i)
    #     sq.append(i)
    #     print(sq)
    # for i in range(4):
    #     print('removed', sq.remove())
    #     print(sq)
    # for i in range(8, 12):
    #     print('added', i)
    #     sq.append(i)
    #     print(sq)
    # while not sq.isEmpty():
    #     print('removed', sq.remove())
    #     print(sq)
    sk = ArrayStack(7,1,8,2,3,5)
    print(sk)
    sortStack(sk)
    print(sk)