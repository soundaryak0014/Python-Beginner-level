#FIND THE POWER OF A NUMBER

#METHOD 1:
Value=int(input("Enter the Value:"))
power=int(input("Enter the power Value:"))
power_of_value=Value**power
print("The power of value:",power_of_value)

#METHOD 2:
Value=int(input("Enter the Value:"))
power=int(input("Enter the power Value:"))
power_of_value=pow(power,Value)
print("The power of value:",power_of_value)

#METHOD 3:
Value=int(input("Enter the Value:"))
power=int(input("Enter the power:"))
result=1
while power>0:
    result=result*Value
    power=power-1
print("The Result is:",result)
