from msgs import Vector3, Spherical


class X150:
    def __init__(self, X110pos: Spherical):
        self.X110pos: Spherical = X110pos
        self.X110rel: Spherical = Spherical(0, 0, 0)

    def update(self, X110rel: Spherical) -> None:
        self.X110rel: Spherical = X110rel

    def getFromWorldFrame(self) -> Spherical:
        return self.X110pos - self.X110rel

    def get_from_X110_frame(self) -> Vector3:
        return Vector3(0, 0, 0) - self.X110rel.to_Vector3()
