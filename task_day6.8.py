print("===WELCOME TO MY CALCULATOR===")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("Please choose what's operation you wanna do : "))

a = int(input("Please give me first number : "))
b = int(input("Please give me second number : "))

if(choice == 1):
	print(a+b)
elif(choice == 2):
	print(a-b)
elif(choice==3):
	print(a*b)
elif(choice==4:
	print(a/b)
else:
	print("you give us invalid choice")


