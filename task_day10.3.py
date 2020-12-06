import re

string=input("Enter a string:")
x=re.findall('[0-9]{1,3}',string)# to serach number 0-9 in a string that have length 1-3
print(x)