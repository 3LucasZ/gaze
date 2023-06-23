from msgs import Vector3


class IMU:
    def __init__(self, hz: float=0.01):
        self.vel: Vector3 = Vector3(0,0,0)
        self.pos: Vector3 = Vector3(0,0,0)
        self.hz: float = hz

    def update(self, acc: Vector3):
        self.pos = self.vel*self.hz + 0.5*acc*self.hz*self.hz
        self.vel = self.vel + acc*self.hz

    def getVel(self):
        return self.vel
    
    def getPos(self):
        return self.pos
    
    def __str__(self) -> str:
        return "{vel:"+str(self.vel)+", pos:"+str(self.pos)+"}"
    
