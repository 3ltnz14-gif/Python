import random
import string

print("hi guys")

length = int(input("\n Enter the length of the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.choices(all, k=length)

password = "".join(temp)

print(password)
