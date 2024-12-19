word = input()[::-1]
i, j = 1, 2
combinations = []

while i < len(word)-1:
    partOne = word[:i]
    while j < len(word):
        partTwo = word[i:j]
        partThree = word[j:]
        # print(partOne, partTwo, partThree)
        combinations.append(partThree + partTwo + partOne)

        j += 1
    
    i += 1
    j = i + 1

print(min(combinations))