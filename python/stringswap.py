a=input("Enter the first string : ")
b=input("Enter the second string : ")
c=b[0]+b[1]+a[2:-1]+a[-1]
d=a[0]+a[1]+b[2:-1]+b[-1]
print("After swapping string is",c,d)

