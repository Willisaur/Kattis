i=int(input())
highestFun = 0
funnestPerson = ""

for ii in range(i):
    a,b = input().split()
    b = int(b)
    if b > highestFun:
        funnestPerson = a
        highestFun = b

print(funnestPerson)
