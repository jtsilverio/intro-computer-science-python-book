class Point:
    def __init__(self, xcoord = 0, ycoord = 0):
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        self.x = xcoord
    
    def sety(self, ycoord):
        self.y = ycoord
    
    def getx(self):
        return self.x

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point()
p.setx(2)
p.sety(2)
p
p.getx()

q = Point()

r = Point(2,3)
r