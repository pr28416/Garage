from random import randint

def bubbleSort(lst):
    for end in range(len(lst)-1, 0, -1):
        noSwap = True
        for i in range(end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                noSwap = False
        if noSwap: return

nums = [i for i in range(10)]
for i in range(len(nums)):
    r = randint(0, len(nums)-1)
    nums[i], nums[r] = nums[r], nums[i]

print('start:', nums)
bubbleSort(nums)
print('end:', nums)