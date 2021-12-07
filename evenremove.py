a=input("Enter the list of numbers :")
b=a.split(',')
c=list(map(int,b))
d=len(c)
for i in range(d) :
	if c[i]%2==0 :
		c.remove(c[i])
print(c)
