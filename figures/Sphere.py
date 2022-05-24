from Ellipsoid import Ellipsoid


class Sphere(Ellipsoid):

    def __init__(self, name, volume, height, diameter, radius, ellipsoid_type, sphere_segment_area: float,
                 sphere_type: str) -> None:
        super().__init__(name, volume, height, diameter, radius, ellipsoid_type)
        self._sphere_segment_area = sphere_segment_area
        self._sphere_type = sphere_type

    def __str__(self):
        return super().__str__() + f", area of sphere segment: {self._sphere_segment_area}, " \
                                   f"type of sphere: {self._sphere_type}"

    def draw_figure(self) -> str:
        return "Drawing the sphere!"
