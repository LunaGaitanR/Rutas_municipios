from algorithm import aStar, best, dijkstra, neighbors

# Definir el nodo inicial y el nodo objetivo
ini = 'Tauramena'
goal = 'Bogotá'

# Obtener el grafo y las posiciones desde neighbors.py
graph = neighbors.getGraph()
position = neighbors.getPosition()

# Ejecutar A* y mostrar el resultado
path_aStar = aStar.aStar(graph, ini, goal, position)
if path_aStar:
    print("Path A* found:", path_aStar)
else:
    print("No path found between", ini, "and", goal)

# Ejecutar Greedy Best-First Search y mostrar el resultado
path_best = best.greedyBestFirstSearch(graph, ini, goal, position)
if path_best:
    print("Path Greedy found:", path_best)
else:
    print("No path found between", ini, "and", goal)

# Ejecutar Dijkstra y mostrar el resultado
path_dijkstra = dijkstra.dijkstra(graph, ini, goal)
if path_dijkstra:
    print("Path Dijkstra found:", path_dijkstra)
else:
    print("No path found between", ini, "and", goal)
