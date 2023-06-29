from X150 import X150
from msgs import get_from_X110_frame, Spherical
from math import *

def test_get
beacon: X150 = X150(Spherical(1,pi/2,pi/2))
beacon.update(Spherical(1,pi/2,pi/2))

assert(beacon.get_from_world_frame()==Spherical(0,0,0))
assert(beacon.get_from_X110_frame()==get_from_X110_frame(0,-1,0))