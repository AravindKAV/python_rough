a=input("Enter the number :")


def factorial(a):
if a<0 :
	print("No Factorial")
	elif(a==0 or a==1) :
		print("0")
else :
	fact=1
	for i in range(a) :
		fact=fact*i
		i++
		return fact
print(
	
