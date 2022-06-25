from QuadrangleBased import QuadrangleBased


class Parallelepiped(QuadrangleBased):

    def __init__(self, name, volume, height, diagonal_len, num_of_edges, parallelepiped_type="unknown") -> None:
        super().__init__(name, volume, height, diagonal_len, num_of_edges)
        self._parallelepiped_type = parallelepiped_type

    def __str__(self):
        return super().__str__() + f", type of parallelepiped: {self._parallelepiped_type}"

    def draw_figure(self) -> str:
        return "Drawing the parallelepiped!"
