from X150 import X150
from msgs import Vector3, Spherical
from math import *

print("Testing: X150")

beacon: X150 = X150(Spherical(1,pi/2,pi/2))
beacon.update(Spherical(1,pi/2,pi/2))

print("T: 1")
assert(beacon.getFromWorldFrame()==Spherical(0,0,0))
assert(beacon.getFromX110Frame()==Vector3(0,-1,0))