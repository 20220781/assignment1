#act 6
from datetime import timedelta 

num1=float(input ('Input distance (meters):'))

h_input= timedelta(hours=float(input ('input time(hour):')))
m_input= timedelta(minutes=float(input ('input time(minutes):')))
s_input= timedelta(seconds=float(input ('input time(second):')))

Time_T=h_input+m_input+s_input
km= num1*0.001
miles= num1*0.000621371
print ('Your speed in meters/sec is',round(float(num1/Time_T.seconds),(6)))
print('Your speed in km/h is',round(float(km/Time_T.seconds*3600),(5)))
print('Your spped in miles/h',round(float(miles/Time_T.seconds*3600),(4)))