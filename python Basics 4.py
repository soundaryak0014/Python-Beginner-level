#REVERSE THE NUMBER
#METHOD 1

Value=int(input("Enter the value:"))
Value2=str(Value)[::-1]
print(Value2)

#METHOD 2
Value=int(input("Enter the Value"))   #123
reverse=0
while Value>0:
    digit=Value%10                    #digit=123%10=3
    reverse=digit+(reverse*10)        #0=3+(0*10)=3
    Value=Value//10                   #123=123//10=12
print(reverse)
                
                                      #12
                                      #3=12%10=2
                                      #3=2+(3*10)=32
                                      #12=12//10=1

                                      #1
                                      #2=1%10=1
                                      #32=1+(32*10)=320
                                      #1=1//10=0
