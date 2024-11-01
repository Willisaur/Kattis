numSquares, index, magicNumber = map(int, input().split())
board = list(map(int, input().split()))
hops = 0
visited = [0] * numSquares

index -= 1 # one-indexed

while index >= 0 and index < numSquares and not visited[index] and board[index] != magicNumber:
    visited[index] = 1
    hops += 1
    index += board[index]

if index < 0:
    print('left')
elif index >= numSquares:
    print('right')
elif board[index] == magicNumber:
    print('magic')
else:
    print('cycle')

print(hops)