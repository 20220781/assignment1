#test time

from datetime import timedelta 
a = timedelta(days=2, hours=6)

b = timedelta(hours=4.5)

c = a + b

print(c.days)

print(c.seconds)

print(c.seconds / 3600)