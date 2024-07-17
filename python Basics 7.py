#PRIME NUMBERS:

Value=int(input("enter the value:"))
count=0
for i in range(2,Value):
    if (Value%i==0):
        count+=1
    
if count==0:
    
    print("it is prime")
else:
    print("it is not prime")

    
print("The program excecuted successfully")
