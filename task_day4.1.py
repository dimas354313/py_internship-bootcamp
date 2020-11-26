''' oke day 4 we learn about list and tuple, tuple is one of data type in python. tuple is immutable so we can't 
modify however, we can reassign the variable if we want to change it we can't use the method like append or remove in tuple
we can see the implementation in the following code
'''
data = ('nama', 'andreas Bimantoro', 'class', '3IA05', 'University', 'standford', 'umur', 20, 'tinggi', 165, 'income', 5000000000)

x = list(data)

reverse_data = data[::-1]

print(data)
print()
print(reverse_data)
print()
print(x)