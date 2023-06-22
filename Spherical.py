from math import sin,cos

from Vector3 import Vector3;

class Spherical:
    def __init__(self, r: float,az: float,el: float):
        self.r=r
        self.az=az
        self.el=el

    def __add__(self, o: Spherical):
        u = self.toVector3()
        v = o.toVector3()

    def toVector3(self):
        x = self.r*sin(self.el)*cos(self.az)
        y = self.r*sin(self.el)*sin(self.az)
        z = self.r*cos(self.el)
        return Vector3(x,y,x)
    
    def __str__(self):
        return("{"+str(round(self.r,5))+","+str(round(self.az,5))+","+str(round(self.el,5))+"}")