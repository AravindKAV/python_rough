a=input("Enter the first set of numbers :")
b=a.split(',')
c=input("Enter the second set of numbers :")
d=c.split(',')
e=len(b)
f=len(d)

g=0
h=0
k=list(map(int,b))
l=list(map(int,d))
if e==f :
	print("Both sets have same number of elements ")
else :
	print("Number of elements of the two sets are different ")
for i in range(e):
	g+=k[i]
for i in range(f):
	h+=l[i]
if g==h :
	print("Sum of the sets are same")
else :
	print("Both the sets have different sums ")
	
for i in range(e):
	if k[i] in l:
		print(k[i],"is in both the sets")
