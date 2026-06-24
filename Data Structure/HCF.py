largest = int(input("Enter the largest number: "))
smallest = int(input("Enter the smallest number: "))

while(smallest):
    store = smallest
    smallest = largest%smallest
    largest = store

print("HCF is", largest)