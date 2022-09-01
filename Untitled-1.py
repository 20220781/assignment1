num1 = 0 # first variable with a default value of zero
num2 = 0 # second variable with a default value of zero

num1 = int(input("Enter First number")) #taking input of first variable
num2 = int(input("Enter Second Number")) #taking unput of second variable

opp= input("What arithemic operation you want to perform,+,-,*,/")


if(opp == '+'):
    result = num1+num2
elif(opp == '-'):
    result = num1-num2
elif(opp == '*'):
    result = num1*num2
elif(opp == '/'):
    result = num1/num2
else:
    print("Wrong Input!!!")

print("the two number is", result)
sum = int(num1) + int(num2) #converting the type of variable and them adding them 

print("The Sum of Two numbers is", sum) #pringting the sum of variables
print("the sum of Two number is %d" %sum) #printing in a different way

result = 0
#print("%d + %d = %d" %(num1, num2, sum))
#Airthemic Operation
#+,-,*,/,%

#print(f"(num1) + (numb2) = (sum)")
# = assignment operator
# == is comparison operator


