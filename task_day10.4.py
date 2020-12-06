import re

list1=['Sun','catchable','Above','TABLE','MOON']
print("List contains:",list1)
print("Words that contains only uppercase letter:",end=' ')
for i in list1:
    if(re.match('[A-Z]*$',i)):#to match only string that contains uppercase letter
        print(i,end=' ')