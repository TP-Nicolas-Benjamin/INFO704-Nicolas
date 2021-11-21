class SimpleUnionFind:
    "A simple way to implement Union Find structure"

    def __init__(self) -> None:
        pass

    def makeSet(self, x):
        x.parent = None

    def find(self, x):
        if x.parent == None:
            return x
        return self.find(x.parent)

    def union(self, x, y):
        xRacine = self.find(x)
        yRacine = self.find(y)
        if xRacine != yRacine:
            xRacine.parent = yRacine
            yRacine.children.append(xRacine)

# NOT FINISHED NOR USED
class EnhancedUnionFind:
    "A better way to implement Union Find"

    def makeSet(self, x):
        x.parent = x
        x.rang = 0

    def union(self, x, y):
        xRacine = SimpleUnionFind.find(x)
        yRacine = SimpleUnionFind.find(y)
        if xRacine != yRacine:
            if xRacine.rang < yRacine.rang:
                xRacine.parent = yRacine
            else:
                yRacine.parent = xRacine
                if xRacine.rang == yRacine.rang:
                    xRacine.rang += 1