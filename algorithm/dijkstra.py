import heapq

def dijkstra(graph, initial, goal):
    # Estructuras
    openSet = [(0, initial)]  # (distancia acumulada, nodo)
    cameFrom = {}
    gCost = {node: float('inf') for node in graph}
    gCost[initial] = 0

    while openSet:
        current_distance, current_node = heapq.heappop(openSet)

        if current_node == goal:
            # Reconstruir el camino
            path = [current_node]
            while current_node in cameFrom:
                current_node = cameFrom[current_node]
                path.append(current_node)
            return path[::-1]  # Devolvemos el camino en orden inverso

        # Ver vecinos
        for neighbor, distance in graph[current_node].items():
            tentative_gCost = current_distance + distance
            if tentative_gCost < gCost[neighbor]:
                cameFrom[neighbor] = current_node
                gCost[neighbor] = tentative_gCost
                heapq.heappush(openSet, (tentative_gCost, neighbor))

    return None  # No se encontró camino
