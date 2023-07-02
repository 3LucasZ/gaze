from math import *

from utils import eq


class Vector3:
    def __init__(self, x: float, y: float, z: float) -> "Vector3":
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __add__(self, o: "Vector3") -> "Vector3":
        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o: "Vector3") -> "Vector3":
        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o: float) -> "Vector3":
        return Vector3(self.x * o, self.y * o, self.z * o)

    def __rmul__(self, o: float) -> "Vector3":
        return Vector3(self.x * o, self.y * o, self.z * o)

    def __str__(self) -> str:
        return (
            "{x:"
            + str(round(self.x, 5))
            + ",y:"
            + str(round(self.y, 5))
            + ",z:"
            + str(round(self.z, 5))
            + "}"
        )

    def __eq__(self, o: "Vector3") -> bool:
        return eq(self.x, o.x) and eq(self.y, o.y) and eq(self.z, o.z)

    def to_Spherical(self) -> "Spherical":
        r: float = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if eq(r, 0):
            return Spherical(0, 0, 0)
        az: float = atan2(self.y, self.x)
        el: float = acos(self.z / r)
        return Spherical(r, az, el)

    def to_arr(self):
        return [self.x, self.y, self.z]


class Spherical:
    def __init__(self, r: float, az: float, el: float) -> "Spherical":
        self.r = r
        self.az = az
        self.el = el

    def __add__(self, o) -> "Spherical":
        u: Vector3 = self.to_Vector3()
        v: Vector3 = o.toVector3()
        return (u + v).to_Spherical()

    def __sub__(self, o) -> "Spherical":
        u: Vector3 = self.to_Vector3()
        v: Vector3 = o.toVector3()
        return (u - v).to_Spherical()

    def __str__(self) -> str:
        return (
            "{r:"
            + str(round(self.r, 5))
            + ",az:"
            + str(round(self.az, 5))
            + ",el"
            + str(round(self.el, 5))
            + "}"
        )

    def __eq__(self, o: "Spherical") -> bool:
        return eq(self.r, o.r) and eq(self.az, o.az) and eq(self.el, o.el)

    def to_Vector3(self) -> "Vector3":
        x: float = self.r * sin(self.el) * cos(self.az)
        y: float = self.r * sin(self.el) * sin(self.az)
        z: float = self.r * cos(self.el)
        return Vector3(x, y, z)
