from IMU import IMU
from msgs import Vector3
from pytransform3d.rotations import quaternion_from_extrinsic_euler_xyz


def test_get_lin_vel(acc: Vector3):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.set_reading(
        acc, Vector3(0, 0, 0), quaternion_from_extrinsic_euler_xyz([0, 0, 0])
    )
    return pigeonIMU.get_lin_vel()


def test_get_lin_pos(acc: Vector3):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.set_reading(
        acc, Vector3(0, 0, 0), quaternion_from_extrinsic_euler_xyz([0, 0, 0])
    )
    return pigeonIMU.get_d_lin_pos()


def test_get_vel():
    assert test_get_lin_vel(Vector3(1, 1, 1)) == Vector3(1, 1, 1)
    assert test_get_lin_vel(Vector3(2, 3, 4)) == Vector3(2, 3, 4)


def test_get_pos():
    assert get_lin_pos(Vector3(1, 1, 1)) == Vector3(0.5, 0.5, 0.5)
    assert get_lin_pos(Vector3(2, 3, 4)) == Vector3(1, 1.5, 2)
