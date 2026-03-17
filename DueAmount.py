total = int(input("How much was the total? "))
paid = int(input("How much was already paid? "))
def due():
    return print("The customer still needs to pay $", total-paid)

due()