def find_max (L):
    if len(L) == 1:
        return L[0]
    print(L)
    v1 = L[0]
    v2 = find_max(L[1:]) 
    if v1 > v2:
        return v1
    else:
        return v2

t = [8,94,13,52,1,24]
print(find_max(t))
