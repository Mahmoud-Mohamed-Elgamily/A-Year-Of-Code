s = input("enter your string here ")
x = list(s)
l = []

for letter in x :

	if letter not in l :
		l.append(letter)

print(l)
