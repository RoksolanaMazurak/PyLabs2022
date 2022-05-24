from CircleBased import CircleBased


class Cone(CircleBased):

    def __init__(self, name, volume, height, diameter, radius, obliquity: str, cone_type: str) -> None:
        super().__init__(name, volume, height, diameter, radius)
        self._obliquity = obliquity
        self._cone_type = cone_type

    def __str__(self):
        return super().__str__() + f", obliquity: {self._obliquity}, type of cone: {self._cone_type}"

    def draw_figure(self) -> str:
        return "Drawing the cone!"
