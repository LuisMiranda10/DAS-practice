"""
Subarray with Given Sum
"""

arr = [1, 4, 0, 0, 3, 10, 5]
soma = 7

left = 0
index_list = []
count = 0

for right, number in enumerate(arr):
    count += number
    
    while count > soma:
        count -= arr[left]
        left += 1
    
    
    if count == soma and index_list != [] and index_list[0] > left:
        index_list[0] = left + 1
        index_list[1] = right + 1
    elif count == soma and index_list == []:
        index_list.insert(0, left + 1)
        index_list.insert(1, right + 1)
    
print(index_list)