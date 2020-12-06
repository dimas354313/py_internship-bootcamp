n=int(input("put your number for multiplying : "))
list1=[1,2,3,4,5]
a=list(map(lambda x:x*n,list1))
print("List before modification:",list1)
print("List after modification:",a)