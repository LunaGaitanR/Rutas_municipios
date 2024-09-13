import heapq

def prim(graph, start_node):
    mst = []  # Lista para almacenar las aristas del árbol de expansión mínima
    total_cost = 0  # Costo total del MST
    visited = set([start_node])  # Conjunto de nodos ya visitados
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(edges)  # Convertir en una cola de prioridad (min-heap)

    while edges:
        cost, node1, node2 = heapq.heappop(edges)

        if node2 not in visited:
            visited.add(node2)
            mst.append((node1, node2, cost))
            total_cost += cost

            # Agregar las aristas del nuevo nodo a la cola de prioridad
            for neighbor, weight in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, node2, neighbor))

    return mst, total_cost
