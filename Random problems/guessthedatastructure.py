from sys import stdin
import heapq
from collections import deque

class operationNode:
    def __init__(self):
        self.stack = []
        self.queue = deque()
        self.heap = []
        self.possibilities = [1] * 3

    def operate(self, o, x):
        if o == 1:
            self.stack.append(x)
            self.queue.append(x)
            heapq.heappush(self.heap, -x)
        else:
            if self.stack: # there are things to pop
                self.possibilities[0] &= (self.stack.pop() == x)
                self.possibilities[1] &= (self.queue.popleft() == x)
                self.possibilities[2] &= (heapq.heappop(self.heap) == -x)
            else:
                self.possibilities = [False, False, False]

        # print(self.possibilities, o, x, self.stack, self.queue, self.heap)

    def outcome(self):
        if sum(self.possibilities) > 1:
            print('not sure')
        elif self.possibilities[0]:
            print('stack')
        elif self.possibilities[1]:
            print('queue')
        elif self.possibilities[2]:
            print('priority queue')
        else:
            print('impossible')

flag = True
n = 0
problem = operationNode()
for line in stdin:
    line = line.strip()
    if flag:
        n = int(line)
        flag = False
    else:
        n -= 1
        operation, number = map(int, line.split())
        problem.operate(operation, number)
        if not n:
            problem.outcome()
            flag = True
            problem = operationNode()
