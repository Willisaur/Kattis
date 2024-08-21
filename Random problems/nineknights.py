knights = 0
board = [input() for i in range(5)]

def checkKnight(i, j):
    coords = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    
    for co in coords:
        x = j-co[0]
        y = i-co[1]
        if not isValid(x, y):
            print("invalid")
            exit()

def isValid(a, b):
    if a < 0 or a > 4 or b < 0 or b > 4:
        return True
    if board[a][b] == '.':
        return True
    return False

for i in range(5):
    for j in range(5):
        print(i, j)
        if board[i][j] == 'k':
            knights += 1
            print(knights, i, j)
            checkKnight(i, j)

print(knights)
if knights == 9:
    print("valid")
else:
    print("invalid")
