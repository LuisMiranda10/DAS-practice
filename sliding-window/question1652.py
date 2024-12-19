# LinK: https://leetcode.com/problems/defuse-the-bomb/description/
# Defuse the Bomb

code = [5,7,1,4]
k = 3

n = len(code)
current_sum = 0
result = [0] * n

for i in range(n):
    current_sum = 0
    if k > 0:
        for j in range(1, k+1):
            current_sum += code[(i+j) % n]
    elif k < 0:
        for j in range(1, abs(k)+1):
            current_sum += code[(i-j+n) % n]
    result[i] = current_sum
    
print(result)