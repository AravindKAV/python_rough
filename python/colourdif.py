s1=input("Enter the first set of colours ")
s2=input("Enter the second set of colours ")
s3=s1.split(',')
s4=s2.split(',')
s5=set(s3)
s6=set(s4)
s7=s5.difference(s6)
print(s7)
