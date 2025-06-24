import math

class circle:
    
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
       return math.pi * self.radius ** 2


c1 = circle(10)
c2 = circle(3)
print(c1.get_area())
print(c2.get_area())