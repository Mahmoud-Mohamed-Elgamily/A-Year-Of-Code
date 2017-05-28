x = int(input("enter your index"))
l = [0 , 1]

for i in range(0,x) :
	l.append(l[i]+l[i+1])
  
print(l[x])	
