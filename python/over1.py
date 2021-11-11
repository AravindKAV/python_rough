a=input("Enter the numbers :")
b=a.split(',')
d=list(map(int,b))
c=len(d)
for i in range(c):
	if d[i]>100:
		d[i]="OVER"
print(d)
	
