#COUNT DIGITS IN A NUMBER
#METHOD1:

Value=int(input("Enter the value:"))
Value2=str(Value)
print(len(Value2))


#METHOD2:
Value=int(input("Enter the Value:"))
Value2=str(Value)
count=0
for i in Value2:
    count+=1
print(count)
