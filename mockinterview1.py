"""
Given a rotated array, find the number of times it was rotated
"""

def numRotates(arr):
    # Assuming len(arr) > 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]: return i+1
    return 0