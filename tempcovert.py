#tempcovert
num1= (int(input("Enter 1. For Celsius to Fahrenheit""Enter 2. For Fahrenheit to Celsius""Enter 3 to Quit:")))
if num1 ==1:
    val=float(input ("Enter Celsius Temperature:"))
    if val<-271.15:
        print ("Note: Temperature below -271.15°C (absolute zero) does not exist on earth!")
    else:
        f = 1.8*float(val)+32
        print ('to Fahrenheit temp is %.2fF'%f)
elif num1==2:
    val=float(input ("Enter Fahrenheit temp:"))
    if val<-459.67:
        print ("Note: Temperature below -459.67°f (absolute zero) does not exist on earth!")
    else:
        c= (float(val)-32)/1.8
        print("after converse temp is %.2fc"%c)
elif num1==3:
    quit
    
