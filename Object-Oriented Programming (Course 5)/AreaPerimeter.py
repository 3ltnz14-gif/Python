class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)
    def circumference(self):
        return 2*3.14*self.radius
    
circ = circle(10)

print(circ.circumference(), "- circumference")
print(circ.area(), "- area")