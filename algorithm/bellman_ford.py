def bellmanFord(graph, initial, goal):
    # Inicialización
    distance = {node: float('inf') for node in graph}
    distance[initial] = 0
    cameFrom = {}

    # Relajación de todas las aristas
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, cost in graph[node].items():
                if distance[node] + cost < distance[neighbor]:
                    distance[neighbor] = distance[node] + cost
                    cameFrom[neighbor] = node

    # Comprobación de ciclos negativos
    for node in graph:
        for neighbor, cost in graph[node].items():
            if distance[node] + cost < distance[neighbor]:
                print("El grafo contiene un ciclo de peso negativo")
                return None

    # Reconstrucción del camino
    path = []
    current_node = goal
    while current_node in cameFrom:
        path.append(current_node)
        current_node = cameFrom[current_node]
    
    if current_node == initial:
        path.append(initial)
        return path[::-1]  # Camino en orden inverso

    return None  # Si no se encontró el camino
