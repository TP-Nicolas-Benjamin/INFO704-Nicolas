from os import link
import networkx as nx
import matplotlib.pyplot as plt

from City import City
from Graph import Graph
from UnionFind import SimpleUnionFind

cities = []

def read_file(file_name: str):
    file = open(file_name, 'r')
    Lines = file.readlines()
    
    id = 0
    for line in Lines:
        l = line.split(" ")
        v = City(id, int(l[0]), int(l[1]) )
        cities.append(v)
        id += 1
    # cities.remove(cities[0])

def getCityFromTo(key: str):
    s = key.split("-")
    return int(s[0]), int(s[1])

def kruskal(g: Graph):
    union = SimpleUnionFind()
    a = []
    for v in g.cities:
        union.makeSet(v)
    
    g.graphDistance = dict(sorted(g.graphDistance.items(), key=lambda item: item[1]))
    for arete in g.graphDistance:
        u,v = getCityFromTo(arete)
        if union.find(g.cities[u]) != union.find(g.cities[v]):
            a.append(arete)
            union.union(g.cities[u], g.cities[v])

    return a

def parcoursKruskal(cycle_array, n: City):
    cycle = cycle_array

    if not n.children:
        cycle.append(n.id)
        return cycle
    else:
        for child in n.children:
            if not(n.id in cycle):
                cycle.append(n.id)
            cycle = parcoursKruskal(cycle, child)

    return cycle


if __name__ == "__main__":
    read_file("Cities20.txt")

    g = Graph(cities)
    
    g.graphDistance = dict(sorted(g.graphDistance.items(), key=lambda item: item[1]))
    tabAretes = kruskal(g)

    noParentNode = g.cities[0]
    for n in g.cities:
        if n.parent == None:
            noParentNode = n
            break

    cycle = parcoursKruskal([], noParentNode)
    cycle.append(noParentNode.id)

    print(f"ARETES TRIÉES :\n{tabAretes}")
    print(f"CYCLE TROUVÉ :\n{cycle}")

    ##### GRAPH #####
    # G = nx.Graph()
    # for n in g.cities:
    #     G.add_node(n.id)

    # for n in g.cities:
    #     if n.parent != None:
    #         G.add_edge(n.id, n.parent.id)
        
    # nx.draw(G, with_labels=True)
    # plt.text(-10,-10, cycle, bbox=dict(fill=False, edgecolor='red', linewidth=2))
    # plt.savefig("parents10.png")
    # plt.show()