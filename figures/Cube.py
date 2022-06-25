from Parallelepiped import Parallelepiped


class Cube(Parallelepiped):

    def __init__(self, name, volume, height, diagonal_len, num_of_edges, parallelepiped_type, cube_type: str) -> None:
        super().__init__(name, volume, height, diagonal_len, num_of_edges, parallelepiped_type)
        self._cube_type = cube_type

    def __str__(self):
        return super().__str__() + f", type of cube: {self._cube_type}"
