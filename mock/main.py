from time import sleep
from msgs import Vector3, Spherical
from X150 import X150
from IMU import IMU
from pytransform3d.transform_manager import TransformManager
from pytransform3d.transformations import transform_from
from pytransform3d.rotations import active_matrix_from_extrinsic_euler_xyz
from math import *

tm = TransformManager()

# xyLoc = position of y in x coordinate frame
# xyPose = pose of y in x coordinate frame
worldBeaconLoc: Vector3 = Spherical(1e10, pi / 8, pi / 8).to_Vector3()
worldBeaconPose = transform_from(
    active_matrix_from_extrinsic_euler_xyz([0, pi / 2, pi / 4]), worldBeaconLoc.to_arr()
)
tm.add_transform("world", "beacon", worldBeaconPose)

localizer: X150 = X150()
baseLocalizerLoc: Vector3 = Vector3(1, 1, 0)
baseLocalizerPose = transform_from(
    active_matrix_from_extrinsic_euler_xyz([0, pi / 2, 0]),
    baseLocalizerLoc.to_arr(),
)
tm.add_transform("base", "X150", baseLocalizerPose)

imu: IMU = IMU()
baseImuLoc: Vector3 = Vector3(-1, -1, 0)
baseImuPose = transform_from(
    active_matrix_from_extrinsic_euler_xyz([0, 0, 0]),
    baseImuLoc.to_arr(),
)
tm.add_transform("base", "imu", baseImuPose)

base_loc: Vector3 = Vector3(0, 0, 0)


# super silly sim
def merge(posImu: Vector3, posLocalizer: Vector3) -> Vector3:
    return (posImu + posLocalizer) * 0.5


# xPosy = position of x from sensor y
while True:
    basePosImu = base_loc + imu.get_d_lin_pos()
    localizerBeaconLoc = localizer.get_reading().to_Vector3()
    beaconLocalizerPose = transform_from(
        active_matrix_from_extrinsic_euler_xyz([0, 0, 0]), localizerBeaconLoc.to_arr()
    )
    tm.add_transform("beacon", "localizer", beaconLocalizerPose)

    basePosLocalizer = tm.get_transform("world", "base")
    basePos = merge(basePosImu, basePosLocalizer)
    sleep(1)
    print(basePos)
