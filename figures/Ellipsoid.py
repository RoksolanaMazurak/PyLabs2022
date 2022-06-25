from CircleBased import CircleBased


class Ellipsoid(CircleBased):

    def __init__(self, name, volume, height, diameter, radius, ellipsoid_type: str) -> None:
        super().__init__(name, volume, height, diameter, radius)
        self._ellipsoid_type = ellipsoid_type

    def __str__(self):
        return super().__str__() + f", ellipsoid type: {self._ellipsoid_type}"

    def draw_figure(self) -> str:
        return "Drawing the ellipsoid!"
