#ARMSTRONG NUMBER:

n=153
n1=n
rev=0
while n>0:
    digit=n%10    
    rev=rev+(digit*digit*digit) 
    n=n//10
    
print(rev)
if n1==rev:

    print(rev, "is armstrong")
else:
    print(rev," is not armstrong")
    
