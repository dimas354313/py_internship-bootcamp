import re

string=input("Enter a word/sentence:")
if(re.search('[0-9]$',string)):#to search number at the end of the senteces
    print("The string contains a number at the end!")
else:
    print("The string does not contain any number at the end!")