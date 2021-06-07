def maxPathSumTriangle(arr):
    for row in range(len(arr)-2, -1, -1):
        for col in range(len(arr[row])):
            arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])
    return arr[0][0]

# arr = [
#     [1],
#     [4, 8],
#     [1, 5, 3],
# ]
# print(maxPathSumTriangle(arr))
with open("input.txt") as f:
    arr = []
    for line in f:
        arr.append(list(map(int, line.split(" "))))
    print(maxPathSumTriangle(arr))
    for i in arr:
        print(i)