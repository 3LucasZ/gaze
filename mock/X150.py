from msgs import Vector3, Spherical


class X150:
    def __init__(self):
        self.reading: Spherical = Spherical(0, 0, 0)

    def set_reading(self, reading: Spherical) -> None:
        self.reading: Spherical = reading

    def get_reading(self) -> Spherical:
        return self.reading
