from CircleBased import CircleBased


class Cylinder(CircleBased):

    def __init__(self, name, volume, height, diameter, radius, bases_type: str, cylinder_type: str) -> None:
        super().__init__(name, volume, height, diameter, radius)
        self._bases_type = bases_type
        self._cylinder_type = cylinder_type

    def __str__(self):
        return super().__str__() + f", type of bases: {self._bases_type}, type of cylinder: {self._cylinder_type}"

    def draw_figure(self) -> str:
        return "Drawing the cylinder!"
