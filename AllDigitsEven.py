print("enter the range to search in ")
x = input("start at > ")
y = input("End at > ")

num = []
for i in range (x , y):
    i = str(i)
    if int(i[0]) % 2 ==0 and int(i[1]) % 2 ==0 and int(i[2]) % 2 ==0 and int(i[3]) % 2 ==0 :
        num.append(i)
print(num)
