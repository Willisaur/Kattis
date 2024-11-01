import sys

flag = True
d = dict()

for line in sys.stdin:
    if line == "\n":
        flag = False
    elif flag:
        v, k = line.split()
        d[k] = v
    else:
        print(d.get(line.strip(), "eh"))