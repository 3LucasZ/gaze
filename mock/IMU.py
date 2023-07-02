from numpy import ndarray
from msgs import Vector3
from pytransform3d.rotations import quaternion_from_extrinsic_euler_xyz


class IMU:
    def __init__(self, hz: float = 0.01):
        self.linVel = Vector3(0, 0, 0)
        self.hz: float = hz
        self.set_reading(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0),
            quaternion_from_extrinsic_euler_xyz([0, 0, 0]),
        )

    def set_reading(self, linAcc: Vector3, angVel: Vector3, ori: ndarray):
        self.dLinPos = self.linVel * self.hz + 0.5 * linAcc * self.hz * self.hz
        self.linVel = self.linVel + linAcc * self.hz
        self.angVel = angVel
        self.ori = ori

    def get_lin_vel(self):
        return self.linVel

    def get_d_lin_pos(self):
        return self.dLinPos

    def __str__(self) -> str:
        return "{linVel:" + str(self.linVel) + ", dLinPos:" + str(self.dLinPos) + "}"
