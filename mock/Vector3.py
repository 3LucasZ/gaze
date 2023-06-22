class Vector3:
    def __init__(self, x: float,y: float,z: float):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return("{"+str(round(self.x,5))+","+str(round(self.y,5))+","+str(round(self.z,5))+"}")