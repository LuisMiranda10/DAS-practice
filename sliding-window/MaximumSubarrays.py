"""
Sliding Window Maximum (Maximum of all subarrays of size K)
"""
array = [20, 10, 30]
k = 1

left = 0
maximum = 0

for right, number in enumerate(array):   
    while right - left + 1 == k:
        print(max(array[left:right+1]))
        left += 1