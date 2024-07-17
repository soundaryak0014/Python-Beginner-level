#FIND ALL DIVISORS OF A NUMBER

value=int(input("Enter the value:"))

for i in range(1,value+1):
    if value%i==0:
        print("The Divisors are:",i)
