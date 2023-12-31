# test conversions
from math import *
import random
from msgs import Vector3, Spherical


def test_conversions():
    assert Spherical(1, pi / 2, pi / 2).to_Vector3() == Vector3(0, 1, 0)
    assert Vector3(1, 1, sqrt(6)).to_Spherical() == Spherical(sqrt(8), pi / 4, pi / 6)


def test_conversions_property():
    for i in range(10):
        print("R:", i + 1)
        x: float = random.uniform(-100, 100)
        y: float = random.uniform(-100, 100)
        z: float = random.uniform(-100, 100)
        assert Vector3(x, y, z) == Vector3(x, y, z).to_Spherical().to_Vector3()
