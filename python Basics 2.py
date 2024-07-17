#LAST DIGIT IN A NUMBER

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=a**b
print(c)
print("The last number is:",abs(c%10))
