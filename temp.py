# def insertionSort(array):

#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
        
#         # Compare key with each element on the left of it until an element smaller than it is found
#         # For descending order, change key<array[j] to key>array[j].        
#         while j >= 0 and key > array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
        
#         # Place key at after the element just smaller than it.
#         array[j + 1] = key
#         print(array)


# data = [90,23,-6,17,111,64,3]
# insertionSort(data)
# print('Sorted Array in des Order:')
# print(data)


# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# s=0
# for x in arr:
#     for y in range(len(x)-1):
#         s += x[y]
# print(s)


# class Q(object):
#     v = 10
#     def __init__(self, x):
#         self.x = x
#     @staticmethod
#     def foo(x):
#         Q.v += 5
#         return x**3+Q.v
#     def bar(self):
#         if (x+Q.v <= 22):
#             raise Exception("Runtime failure!")
#         return "Success!";

# x=2
# x=Q.foo(x)
# instance=Q(x)
# print(instance.bar())

# n = 85

# binary = '{:b}'.format(n)
# print(binary)
# o=0;
# z=0;
# for bit in binary:
#     if (bit=='0'):
#         o += 1
#     else: z += 1
# if o==z:
#     print('check passed')
# else: print('check failed')

# pb=-1
# failed = False
# while n > 0:
#     bit = n & 1
#     n = n >> 1
#     if (pb!=-1 and pb == bit):
#         failed = True
#         break
# if (not failed):
#     print("Check passed")
# else: print("Check failed")

# binary = '{:b}'.format(n)
# print(binary)
# pb=''
# failed = False
# for bit in binary:
#     if (pb!='' and pb == bit):
#         failed = True
#         break
#     pb=bit
# if (not(failed)):
#     print("Check passed")
# else: print("check failed")

# def isSorted(arr, startIndex, lastIndex):
#     midIndex = int((startIndex+lastIndex)/2)
#     if (not isSorted(arr, startIndex, midIndex)):
#         return False
#     if (not isSorted(arr, midIndex+1, lastIndex)):
#         return False
#     return (arr[midIndex] <= arr[midIndex+1])

# arr = [i for i in range(6, 17)]
# print(isSorted(arr, 0, len(arr)-1))

# def mystery(x): # returns number of 1s in binary representation
#     count = 0
#     while (x != 0):
#         x = x & (x-1)
#         count += 1
#     print('x=', x)
#     return count

# print(mystery(1))
# print(mystery(2))
# print(mystery(3))
# print(mystery(4))
# print(mystery(5))
# print(mystery(6))
# print(mystery(7))
# print(mystery(8))



def sjh(a):
    for i in range(len(a)):
        foo = i
        for j in range(i+1, len(a)):
            if (a[foo] < a[j] and a[j] % 2 == 0):
                foo = j
        a[i], a[foo] = a[foo], a[i]
    return a

def other(s):
    a = list()
    for l in s:
        a.append(ord(l)-ord('a'))
    p = sjh(a)
    rec=""
    for a in p:
        rec += chr(a+ord('a'))
    return rec

print(other('dead'))

# def foo(x):
#     lhs = -1*(8*x)-1
#     return lhs==(~(x << 3))

# print(all([foo(x) for x in range(1, 100001)]))

# d=4.55
# d2=3.42
# j=int(d*100+d2)
# print(j)



# class Test1:
#     def change(self, n):
#         n *= 3
#         print(n, end='')

# class Test2(Test1):
#     def change(self, n):
#         n += 2
#         super().change(n)
#         print(n, end='')

# t = Test2()
# t.change(2)