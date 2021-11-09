import numpy as np

class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.indexTab = {}
        self.graphNodes = {}
        self.graphDistance = {}

        for i in range(len(nodes)):
            self.indexTab[i] = 0

        for i in range(len(nodes)):
            self.graphNodes[i] = []
            for j in range(len(nodes)):
                if i != j:
                    self.graphNodes[i].append(j)

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    self.graphDistance[f"{i}-{j}"] = nodes[i].distanceToCity(nodes[j])

        # print("________ index tab ________")
        # print(self.indexTab)
        # print("_______ graph nodes _______")
        # print(self.graphNodes)
        # print("_____ graph distances _____")
        # print(self.graphDistance)