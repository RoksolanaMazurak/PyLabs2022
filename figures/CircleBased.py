
from SpacialFigures import SpacialFigures


class CircleBased(SpacialFigures):

    def __init__(self, name, volume, height, diameter: float, radius: float) -> None:
        super().__init__(name, volume, height)
        self._diameter = diameter
        self._radius = radius

    def __str__(self):
        return super().__str__() + f", diameter: {self._diameter}, radius: {self._radius}"

    def draw_figure(self) -> str:
        return "Drawing the circle!"
