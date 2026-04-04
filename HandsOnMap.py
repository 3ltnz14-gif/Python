num1 = [1, 2, 3]
num2 = [4, 5, 6]
result = map(lambda x, y: x + y, num1, num2)
print("Addition of the two lists:")
print(list(result))

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n**2
square = list(map(sq, nums))
print("The square of the numbers in list:")
print(square)