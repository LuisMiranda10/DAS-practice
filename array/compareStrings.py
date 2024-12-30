def compare_strings(hasherA, hasherB, number_of_common_features):
    for char in hasherA:
        if char in hasherB:
            number_of_common_features += min(hasherA[char], hasherB[char])
    return number_of_common_features
                
def count_hasher(word):
    hasher = {}
    for char in word:
        hasher[char] = 1 + hasher.get(char, 0)
    return hasher 

def getMaxInformation(dataset, max_common_features):
    number_of_common_features = 0
    information_gain = 0

    for i in range(len(dataset)):
        hasherA = count_hasher(dataset[i])
        for j in range(i+1, len(dataset)):
            hasherB = count_hasher(dataset[j])
            compare_strings(hasherA, hasherB, number_of_common_features)
            
            if number_of_common_features <= max_common_features:
                information_gain = max(information_gain, abs(len(dataset[i])-len(dataset[j])))

    return information_gain

n = int(input())
max_common_features = 1
dataset = [input().strip() for _ in range(n)]
print(getMaxInformation(dataset, max_common_features))