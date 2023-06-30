from IMU import IMU
from msgs import Vector3


def get_vel(acc: Vector3):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.set_reading(acc)
    return pigeonIMU.get_vel()


def get_pos(acc: Vector3):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.set_reading(acc)
    return pigeonIMU.get_pos()


def test_get_vel():
    assert get_vel(Vector3(1, 1, 1)) == Vector3(1, 1, 1)
    assert get_vel(Vector3(2, 3, 4)) == Vector3(2, 3, 4)


def test_get_pos():
    assert get_pos(Vector3(1, 1, 1)) == Vector3(0.5, 0.5, 0.5)
    assert get_pos(Vector3(2, 3, 4)) == Vector3(1, 1.5, 2)
