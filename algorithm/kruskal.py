class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    # Lista de aristas (nodo1, nodo2, peso)
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))
    
    # Ordenar aristas por peso
    edges.sort()

    # Crear la estructura Union-Find
    uf = UnionFind(graph.keys())

    mst = []
    total_cost = 0

    # Construir el MST
    for weight, node1, node2 in edges:
        if uf.find(node1) != uf.find(node2):
            uf.union(node1, node2)
            mst.append((node1, node2, weight))
            total_cost += weight

    return mst, total_cost
