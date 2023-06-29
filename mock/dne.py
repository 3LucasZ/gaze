from msgs import Spherical, get_from_X110_frame
from math import *


print(Spherical(1, pi / 2, pi / 2).to_Vector3())
print(get_from_X110_frame(0, 1, 0).to_Spherical())
print(get_from_X110_frame(1, 1, sqrt(6)).to_Spherical())
