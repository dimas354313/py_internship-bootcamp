dt_python_class = {'jamal', 'smith', 'andreas', 'gilang', 'thomas'}

dt_frontend_class = {"dimas", "eko", "john", "michael", "gilang", "thomas", "andreas"}

enroll_two_class = dt_frontend_class & dt_python_class

print(enroll_two_class)

print(dt_python_class - dt_frontend_class)

print(dt_frontend_class - dt_python_class)