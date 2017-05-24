x = [2 , 3 , 4 , 1 , 5 ]
z = []
for num in x[:]:
	z.append(min(x))
	x.remove(min(x))
print(z)