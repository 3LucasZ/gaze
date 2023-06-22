#test conversions
from math import pi
import random
from msgs import Vector3, Spherical

print("T: 1")
print(Spherical(1,pi/2,pi/2).toVector3())
print(Vector3(0,1,0).toSpherical())

print("T: 2")
assert(Spherical(1,pi/2,pi/2).toVector3() == Vector3(0,1,0))
#assert(Spherical(2,pi/2,pi/2).toVector3() == Vector3(0,1,0))

for i in range(10):
    print("R:",i+1)
    x: float = random.uniform(-100,100)
    y: float = random.uniform(-100,100)
    z: float = random.uniform(-100,100)
    assert(Vector3(x,y,z)==Vector3(x,y,z).toSpherical().toVector3())

