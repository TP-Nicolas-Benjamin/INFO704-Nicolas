import networkx as nx
import matplotlib.pyplot as plt

from City import City
from Graph import Graph
from UnionFind import SimpleUnionFind

cities = []
links = []
base = City()

def read_file(file_name: str):
    global base
    # Using readlines()
    file = open(file_name, 'r')
    Lines = file.readlines()
    
    # Strips the newline character
    for line in Lines:
        l = line.split(" ")
        v = City( int(l[0]), int(l[1]) )
        cities.append(v)
    
    base = cities[0]
    # cities.remove(cities[0])

def link_cities(cities: list[City]):
    for i in range(len(cities)):
        dist = cities[i].distanceToCity(cities[(i+1)%len(cities)])
        links.append(dist)

def getCityFromTo(key: str):
    s = key.split("-")
    return int(s[0]), int(s[1])

def kruskal(g: Graph):
    union = SimpleUnionFind()
    #####
    # print(list(g.graphDistance.keys())[0])
    # city_from, city_to = getCityFromTo(list(g.graphDistance.keys())[0])
    # print(city_from)
    # print(city_to)
    # print(g.graphDistance[f"{city_from}-{city_to}"])
    #####
    a = []
    for v in g.nodes:
        union.makeSet(v)
    
    g.graphDistance = dict(sorted(g.graphDistance.items(), key=lambda item: item[1]))
    for arete in g.graphDistance:
        u,v = getCityFromTo(arete)
        if union.find(g.nodes[u]) != union.find(g.nodes[v]):
            a.append(arete)
            union.union(g.nodes[u], g.nodes[v])

    return a


if __name__ == "__main__":
    read_file("Cities10.txt")
    link_cities(cities)

    g = Graph(cities)
    
    print(dict(sorted(g.graphDistance.items(), key=lambda item: item[1])))

    a = kruskal(g)
    print(a)

    #####
    G = nx.Graph()
    for i in range(len(cities)):
        G.add_node(i)
    
    for arete in a:
        u,v = getCityFromTo(arete)
        G.add_edge(u,v)
        
    nx.draw(G, with_labels=True)
    plt.savefig("img.png")
    plt.show()