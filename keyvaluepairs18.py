student = {'name': 'John', 'age':'25','courses' : ['Math', 'CompSci']}

student['phone'] = '555-5555'


print(student.get('phone','Not Found'))


#section 2


student = {'name': 'John', 'age':'25','courses' : ['Math', 'CompSci']}

student['phone'] = '555-5555'
student['name'] = 'Jane'


print(student)


#section 3



student = {'name': 'John', 'age':'25','courses' : ['Math', 'CompSci']}

age = student.pop('age')

print(student)
print(age)


#section 4



student = {'name': 'John', 'age':'25','courses' : ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)
