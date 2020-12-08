def evenfilter(a):
    if(a%2!=0):
        return True
    else:
        return False
l=[10,7,8,15,14,18,17,56,89,19,35,32,56,754]
print("List:",l)
b=list(filter(evenfilter,l))
print("List of odd numbers:",b)