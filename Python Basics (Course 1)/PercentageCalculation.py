print("Enter marks obtained in each of these subjects:")
math = int(input("Maths:"))
english = int(input("English:"))
science = int(input("Science:"))
social = int(input("Social Studies:"))

sum = math + english + science + social

perc = (sum/400)*100

print("Final Mark: (", perc, "/ 100 )!")