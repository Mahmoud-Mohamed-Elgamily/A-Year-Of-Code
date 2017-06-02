(x,y) = int(input("1 >")) , int(input("2 >"))

p = []

for i in range (0,x+1):
    l = []
    for j in range (0,y+1):
        l.append(i*j)
    p.append(l)

print(p)
