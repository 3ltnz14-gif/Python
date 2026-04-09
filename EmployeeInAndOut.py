class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def createobj():
    print("Making Object...")
    obj = employee()
    print("Function end")
    return obj

print("Calling createobj()")
obj = createobj()
print("Program end...")