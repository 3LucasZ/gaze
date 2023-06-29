from msgs import get_from_X110_frame


class IMU:
    def __init__(self, hz: float = 0.01):
        self.vel: get_from_X110_frame = get_from_X110_frame(0, 0, 0)
        self.pos: get_from_X110_frame = get_from_X110_frame(0, 0, 0)
        self.hz: float = hz

    def update(self, acc: get_from_X110_frame):
        self.pos = self.vel * self.hz + 0.5 * acc * self.hz * self.hz
        self.vel = self.vel + acc * self.hz

    def get_vel(self):
        return self.vel

    def get_pos(self):
        return self.pos

    def __str__(self) -> str:
        return "{vel:" + str(self.vel) + ", pos:" + str(self.pos) + "}"
