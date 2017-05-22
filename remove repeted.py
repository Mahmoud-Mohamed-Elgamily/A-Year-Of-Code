s = input("enter your string here ")
x = list(s)
z = []

for letter in x :

	if letter not in z :
		z.append(letter)

print(z)
