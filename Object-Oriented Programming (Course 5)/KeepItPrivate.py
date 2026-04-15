class myClass:
    __privatevar = 27
    def __privMethod(self):
        print("I'm inside class 'myClass'.")
    def hello(self):
        print(myClass.__privatevar)

foo = myClass()

foo.hello()
foo.__privMethod