num = int(input("You want odd and even number under what value?\n"))

odd_list = [i for i in range(num) if i%2 != 0]
print("List of odd numbers;", odd_list, "\n")

even_list = [i for i in range(num) if i%2 == 0]
print("List of even numbers;", even_list, "\n")

fruits = ["apple", "banana", "mango", "papaya", "grapes"]
Fruits = [x[0].upper() + x[1:] for x in fruits]
print("Fruits as proper nouns:\n", Fruits)