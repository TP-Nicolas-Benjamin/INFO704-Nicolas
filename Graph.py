import numpy as np

class Graph:
    def __init__(self, cities) -> None:
        self.cities = cities
        self.graphDistance = {}

        for i in range(len(cities)):
            for j in range(i, len(cities)):
                if i != j:
                    self.graphDistance[f"{i}-{j}"] = cities[i].distanceToCity(cities[j])