total = int(input("How much was the total? "))
paid = int(input("How much was already paid? "))
def due(x, y):
    return print("The customer still needs to pay $", x-y)

due(total, paid)