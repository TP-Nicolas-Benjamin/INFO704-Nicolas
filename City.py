import math
from os import name

class City:
    "A city is placed at a (X, Y)"

    def __init__(self, id, x=0, y=0) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.children = []

    def distanceToCity(self, city):
        return math.sqrt((city.x - self.x)**2 + (city.y - self.y)**2)

    def distanceToXY(self, x, y):
        return math.sqrt((x - self.x)**2 + (y - self.y)**2)