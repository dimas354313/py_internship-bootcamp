list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28]
print("List:",list1)
a=list(filter(lambda x:(x%2==0),list1))
print("Count of even numbers in the list:",len(a))