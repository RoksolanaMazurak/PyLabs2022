from SpacialFigures import SpacialFigures


class QuadrangleBased(SpacialFigures):

    def __init__(self, name, volume, height, diagonal_len: float, num_of_edges: int) -> None:
        super().__init__(name, volume, height)
        self._diagonal_len = diagonal_len
        self._num_of_edges = num_of_edges

    def __str__(self):
        return super().__str__() + f", length of diagonals: {self._diagonal_len}, number of edges: {self._num_of_edges}"

    def draw_figure(self) -> str:
        return "Drawing the quadrangle!"
