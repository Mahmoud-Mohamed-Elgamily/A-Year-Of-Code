import random

def guess(x):

	y=random.randint(0,9)

	if x == y :
		print("exactly right")
	elif x > y :
		print("too high try again :D")
	else :
		print("too low try again :D")

print("Enter a number from 0 - 9 \nEnter 'exit' when done")
while True:
	z = input("\nyour input >")
	if z == 'exit':
		break
	else:
		guess(int(z))
		

