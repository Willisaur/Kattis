answers = dict()

def solve(currentString = "4", numberOfFours = 1, operators = ['+','-','*','//']):
    # make a choice
    if numberOfFours < 4:
        for operator in operators:
            solve(f"{currentString} {operator} 4", numberOfFours+1)

    # check for solution
    if numberOfFours == 4:
        answer = eval(currentString)
        answers[answer] = f"{currentString} = {answer}"

solve()

for i in range(int(input())):
    print(answers.get(int(input()), "no solution").replace('//', '/'))