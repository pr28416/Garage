class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        arr = []
        head = self
        while head:
            arr.append(head.val)
            head = head.next
        return f'[{", ".join(list(map(str, arr)))}]'

    def __repr__(self):
        return f'<ListNode v: {self.val}, hasNext: {self.next is not None}>'

def listgen(arr):
    head = ListNode()
    trav = head
    for i in arr:
        trav.next = ListNode()
        trav = trav.next
        trav.val = i
    return head.next

def removeDups(head):
    if not head: return head
    seen = {head.val}
    trav = head
    while trav.next:
        if trav.next.val in seen:
            trav.next = trav.next.next
        else:
            seen.add(trav.next.val)
            trav = trav.next
    return head

def kthToLast(head, k):
    p1, p2 = head, head
    for _ in range(k):
        if not p2: return None
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def deleteMiddleNode(middle):
    trav = middle
    prev = None
    while trav.next:
        trav.val = trav.next.val
        prev = trav
        trav = trav.next
    prev.next = None

def partition(head, x):
    lessEnd, greaterEnd = ListNode(), ListNode()
    lessStart, greaterStart = lessEnd, greaterEnd
    trav = head
    while trav:
        if trav.val < x:
            lessEnd.next = ListNode()
            lessEnd = lessEnd.next
            lessEnd.val = trav.val
        else:
            greaterEnd.next = ListNode()
            greaterEnd = greaterEnd.next
            greaterEnd.val = trav.val
        trav = trav.next
    lessEnd.next = greaterStart.next
    return lessStart.next

def sumLists(one, two):
    sm = ListNode()
    hd = sm
    carry = 0
    while one and two:
        sm.next = ListNode(one.val + two.val + carry)
        sm = sm.next
        carry = sm.val // 10
        sm.val %= 10
        one = one.next
        two = two.next
    rem = one or two
    while rem:
        sm.next = ListNode(rem.val + carry)
        sm = sm.next
        carry = sm.val // 10
        sm.val %= 10
        rem = rem.next
    if carry:
        sm.next = ListNode(carry)
    return hd.next

def checkPalindrome(head):
    trav = head
    prev = None
    while trav:
        prev = ListNode(trav.val, prev)
        trav = trav.next
    trav = head
    while trav or prev:
        if not (trav and prev) or trav.val != prev.val: return False
        trav = trav.next
        prev = prev.next
    return True

def intersection(one, two):
    st = set()
    trav = one
    while trav:
        st.add(trav)
        trav = trav.next
    trav = two
    while trav:
        if trav in st: return True
        trav = trav.next
    return False

def loopDetection(head):
    st = set()
    trav = head
    while trav:
        if trav in st: return trav
        st.add(trav)
        trav = trav.next
    return head

if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(5)))))
    # removeDups(head)
    # print(head)
    # head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(5)))))
    # removeDups(head)
    # print(head)
    # head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(2)))))
    # removeDups(head)
    # print(head)
    # head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1)))))
    # removeDups(head)
    # print(head)
    # head = ListNode(1, ListNode(2, ListNode(22, ListNode(-2, ListNode(-1)))))
    # removeDups(head)
    # print(head)
    # head = listgen([1,2,3,4,5])
    # print(*[kthToLast(head, i).val for i in range(1, 6)])
    # head = listgen([1,2])
    # print(*[repr(kthToLast(head, i)) for i in range(1, 6)])
    # head = listgen([1,2,3,4,5])
    # deleteMiddleNode(head.next.next.next)
    # print(head)
    # head = listgen([3,5,8,5,10,2,1])
    # print(partition(head, 5))
    # one = listgen([7,1,6])
    # two = listgen([5,9,2])
    # print(sumLists(one, two))
    # one = listgen([6,1,7])
    # two = listgen([2,9,5])
    # print(sumLists(one, two))
    # print(checkPalindrome(listgen([1,2,3,2,1])))
    # print(checkPalindrome(listgen([1,2,3,2,2])))
    # print(checkPalindrome(listgen([1,2,1])))
    # print(checkPalindrome(listgen([1])))
    # print(checkPalindrome(listgen([2,2,1])))
    # print(checkPalindrome(listgen([2,2])))
    # intersect = listgen([5,6,7])
    # one = listgen([1,0])
    # one.next.next = intersect
    # two = listgen([2,3,4])
    # two.next.next.next = intersect
    # print(intersection(one, two))
    one = listgen(['A','B'])
    loop = listgen(['C','D','E'])
    loop.next.next.next = loop
    one.next = loop
    print(repr(loopDetection(one)))