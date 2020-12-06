import re

list1=['sun','catchable','above','table','moon']
print("List contains:",list1)
print("Words in the list containing 'ab':",end=' ')
for i in list1:
    if(re.search('ab',i)):# to search each items that have ab letter
        print(i,end=' ')