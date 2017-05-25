# 1634 >> 1^4 + 6^4 + 3^4 + 4^4 = 1634 then this number is armstrong number
x = int(input("enter your num... "))
r = x 
x = str(x)
x = map(int , x)

s = 0
z = len(x)
print(z)
for n in x :
	s = s + n**z
print(s)
if s == r :
	print("The number ",r," is Armstrong number")
else : 
	print("Not an Armstrong number")
