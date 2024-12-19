"""
Smallest subarray with sum greater than a given value
"""

arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
x = 280

left = 0
smallest_subarray = float('inf')
sum_nums = 0

for right, number in enumerate(arr):
    sum_nums += number
    
    while sum_nums > x:
            smallest_subarray = min(smallest_subarray, right - left + 1)
            sum_nums -= arr[left]
            left += 1

print(smallest_subarray)