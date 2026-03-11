class Shape:
    def __init__(self, color):
        self.color = color
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super(Circle, self).__init__(color)
        self.radius = radius
    def get_area(self):
        res = 3.14 * (self.radius ** 2)
        return res
    
circle = Circle("red", 5)
print(circle.get_area())