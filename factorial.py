def fact(N):
	if N == 1 :
		return 1 
	N = N*fact(N-1)
	return N

x = int(input("enter the number to get factorial "))
print(fact(x))