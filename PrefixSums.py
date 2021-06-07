# Numbers
numbers = [2, 8, 9, 11, 12, 26, 27, 29, 33, 36, 37, 42, 44, 46, 47, 52, 56, 57, 58, 60, 61, 64, 68, 70, 72, 73, 76, 77, 78, 80, 82, 83, 95, 96, 98, 99]

# Generate prefix sum array
sums = [0] * (len(numbers)+1)
for i in range(len(numbers)):
    sums[i+1] = sums[i] + numbers[i]

# Find sum of numbers in given index range
# rangeSum = sums[29] - sums[14]
# rangeSum = sums[24] - sums[3]
rangeSum = sums[36] - sums[0]
print(rangeSum)

