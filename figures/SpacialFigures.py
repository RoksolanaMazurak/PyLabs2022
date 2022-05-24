from abc import ABC, abstractmethod


class SpacialFigures(ABC):

    def __init__(self, name: str, volume: float, height: float) -> None:
        self._name = name
        self._volume = volume
        self._height = height

    def __str__(self):
        return f"Name of figure is: {self._name}, volume: {self._volume}, height: {self._height}"

    @abstractmethod
    def draw_figure(self) -> str:
        pass
