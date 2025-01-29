s = input()

l = [s[0]]

def patience(ch):
    # patience sort with binary search
    i = 0
    j = len(l)-1

    while i <= j:
        k = (i + j) // 2
        # print(i, k, j, s[i], s[k], s[j])
        if ord(ch) > ord(l[k]):
            i = k+1
        else:
            j = k-1

    return i # return least index where ch >= l[i]

for ch in s:
    if ord(ch) > ord(l[-1]):
        l.append(ch)
    else:
        # print(ch, patience(ch))
        l[patience(ch)] = ch
        # print(l)

print(26-len(l))