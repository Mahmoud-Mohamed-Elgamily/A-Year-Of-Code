import math
C = 50
H = 30
D = str(input("> "))
D = D.split(",")
Q = []

for i in D :

    Q.append(int(math.sqrt((2 * C * int(i))/H)))
    
print(Q)
