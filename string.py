


from ast import Try
from re import S
from warnings import catch_warnings

try:
  str_input = int(input('Input a string:'))
except:
  print("The string is not an integer.")