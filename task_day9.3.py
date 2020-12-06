list1=[1,2,36,90,18,60]
print("List:",list1)
a=list(filter(lambda x:(x%9==0),list1))
print("Elements in list that are divisible by 9:",a)