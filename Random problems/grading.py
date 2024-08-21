grades = list(map(int, input().split() + [0]))
g = int(input())
for i in range(len(grades)):
    if g >= grades[i]:
        print(chr(65+i))
        exit()
