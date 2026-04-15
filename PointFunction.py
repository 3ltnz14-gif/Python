class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def returnCoords(self):
        return self.x, self.y
    
p = point(12, 10)
print(p.returnCoords())