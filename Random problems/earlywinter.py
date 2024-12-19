numYears, lastYear = map(int, input().split())
years = list(map(int, input().split()))

for i in range(numYears):
    if years[i] <= lastYear:
        print(f"It hadn't snowed this early in {i} years!")
        exit()

print('It had never snowed this early!')