from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print(x)
    @abstractmethod
    def task(self):
        print("def task(self):\n    print('def task(self): ...')")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)