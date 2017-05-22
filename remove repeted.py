s = input("enter your string here ")
x = []
z = []

for ch in s :
	x.append(ch)

for letter in x :
	
	if letter not in z :
		print (letter , end = '')
		z.append(letter)
		 
	
