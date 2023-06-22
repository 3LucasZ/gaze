from math import sin,cos

from Vector3 import Vector3;

class Spherical:
    def __init__(self, r: float,az: float,el: float):
        self.r=r
        self.az=az
        self.el=el

    def __add__(self, o):
        u: Vector3  = self.toVector3()
        v: Vector3 = o.toVector3()

    def toVector3(self):
        x: float = self.r*sin(self.el)*cos(self.az)
        y: float = self.r*sin(self.el)*sin(self.az)
        z: float = self.r*cos(self.el)
        return Vector3(x,y,z)
    
    def __str__(self):
        return("{"+str(round(self.r,5))+","+str(round(self.az,5))+","+str(round(self.el,5))+"}")