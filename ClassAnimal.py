from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk & run")
        
class Snake(Animal):
    def move(self):
        print("I can crawl")
        
class Dog(Animal):
    def move(self):
        print("I can bark")
        
class Lion(Animal):
    def move(self):
        print("I can roar")

r = Human()
r.move()
k = Snake()
k.move()
r = Dog()
r.move()
k = Lion()
k.move()