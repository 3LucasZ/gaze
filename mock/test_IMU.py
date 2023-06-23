from IMU import IMU
from msgs import Vector3 

print("Testing: IMU")

pigeonIMU: IMU = IMU(1) 
pigeonIMU.update(Vector3(1,1,1))

print("T: 1")
assert(pigeonIMU.getVel()==Vector3(1,1,1))
assert(pigeonIMU.getPos()==Vector3(0.5,0.5,0.5))