import re

string=input("Make your password:")
if(re.match('^[a-z,A-Z,0-9]*$',string)):
    print("password accepted!")
else:
    print("password rejected!")
    print("make sure your password consist of (a-z,A-Z,and0-9)")