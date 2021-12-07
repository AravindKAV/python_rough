a=input("Enter the sentence :")
b=a.split(' ')
d=set(b)
for i in d :
	print(i,"occurs",b.count(i),"times in the sentence")
	
