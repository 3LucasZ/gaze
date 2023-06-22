from math import pi
from Spherical import Spherical
from Vector3 import Vector3


a: Spherical = Spherical(1,pi/2,pi/2)
b: Vector3 = a.toVector3()

print(a)
print(b)

