# PALINDROME:
value=int(input("Enter the value:"))
value2=value
rev=0
while value>0:
    digit=value%10              #digit=123%10=3,2,1
    rev=digit+(rev*value)       #0=3+(0*123)=3,2+(3*12)=38,1+(38+1)=39
    value=value//10             #123=123//10=12,1
if value2==rev:
    print(rev, "is PALINDROME")
else:
    print(rev, "is NOT PALINDROME")
