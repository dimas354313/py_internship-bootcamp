a=0
b=1
n=5
print("Fibonacci Series:")
c=n
while(n>(c/2)):
    subb=lambda a,b:a+b
    print(a,b,end=" ")
    a=subb(a,b)
    b=subb(a,b)
    n=n-1