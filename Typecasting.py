name = "Elijah"
age = 12
is_student = True
weight = 45.5

print("Name:", name)
print("Data Type of name is:", type(name))

print("Age:", age)
print("Data Type of age is:", type(age))

print("is_student =", is_student)
print("is_student type:", type(is_student))

print("Weight:", weight)
print("Data Type of weight is:", type(weight))

print("\nAfter typecasting:")
age = str(age)
print("Age:", age, type(age))
weight = int(weight)
print("Weight:", weight, type(weight))