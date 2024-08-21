n, k = list(map(int, input().split()))
accum = 0
for i in range(k):
    accum += int(input())
p_max = (3*(n-k) + accum)/n
p_min = (-3*(n-k) + accum)/n
print(f"{p_min} {p_max}")
