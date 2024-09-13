from algorithm import aStar, best, dijkstra, bellman_ford, neighbors
from static import show

show.draw()

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
path = aStar.aStar(graph,ini,goal,neighbors.getPosition())

show.draw()

if path:
    print("Path A* found:", path)
else:
    print("No path found between", ini, "and", goal)

# Ejecutar Dijkstra y mostrar el resultado
path_dijkstra = dijkstra.dijkstra(graph, ini, goal)
if path_dijkstra:
    print("Path Dijkstra found:", path_dijkstra)
else:
    print("No path found between", ini, "and", goal)

# Ejecutar Bellman-Ford y mostrar el resultado
path_bellman_ford = bellman_ford.bellmanFord(graph, ini, goal)
if path_bellman_ford:
    print("Path Bellman-Ford found:", path_bellman_ford)
else:
    print("No path found between", ini, "and", goal)