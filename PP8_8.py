class Point:
    def __init__(self, xcoord = 0, ycoord = 0):
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        self.x = xcoord
    
    def sety(self, ycoord):
        self.y = ycoord
    
    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Vector(Point):    
    def __add__(self, o):
        return(self.x + o.x,
               self.y + o.y)
    
    def __mul__(self, o):
        return((self.x * o.x) + (self.y * o.y))

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 3)
v2 = Vector(-2, 4)
v1 + v2
v1 * v2
v1