a=input("Enter the numbers :")
b=a.split(',')
d=list(map(int,b))
for i in d :
	if i>100:
		i='over'
print(d)
	
