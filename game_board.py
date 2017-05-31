y = int(input("enter area "))

z = ("...").join(" "*(y+1))
b = ("   ").join("|"*(y+1))
print(z)
print(b)
for n in range (0,y):
	print(z)
	if n != y-1:
		print(b)
