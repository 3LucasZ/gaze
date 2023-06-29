from IMU import IMU
from msgs import get_from_X110_frame


def get_vel(acc: get_from_X110_frame):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.update(acc)
    return pigeonIMU.get_vel()


def get_pos(acc: get_from_X110_frame):
    pigeonIMU: IMU = IMU(1)
    pigeonIMU.update(acc)
    return pigeonIMU.getPos()


def test_get_vel():
    assert get_vel(get_from_X110_frame(1, 1, 1)) == get_from_X110_frame(1, 1, 1)
    assert get_vel(get_from_X110_frame(2, 3, 4)) == get_from_X110_frame(2, 3, 4)


def test_get_pos():
    assert get_pos(get_from_X110_frame(1, 1, 1)) == get_from_X110_frame(0.5, 0.5, 0.5)
    assert get_pos(get_from_X110_frame(2, 3, 4)) == get_from_X110_frame(1, 1.5, 2)
