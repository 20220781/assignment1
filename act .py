num1= int(input('enter the first number'))
num2= int(input('enter the second number'))

if num1%2==0:
   result= num1*num2
elif num1%3==0:
    result= num1*num2
elif num2%2==0:
    result= num1*num2
elif num2%3==0:
    result= num1*num2
else:
    result= num1+num2
print (result)

