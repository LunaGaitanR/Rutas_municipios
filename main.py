from algorithm import aStar, best, dijkstra, bellman_ford, kruskal, prim, neighbors
from static import show
import sys

# Definir el nodo inicial y el nodo objetivo
ini = 'Tauramena'
goal = 'Bogotá'

# Obtener el grafo y las posiciones desde neighbors.py
graph = neighbors.getGraph()
position = neighbors.getPosition()

# Ejecutar los algoritmos de búsqueda y mostrar los resultados
path_aStar = aStar.aStar(graph, ini, goal, position)
path_best = best.greedyBestFirstSearch(graph, ini, goal, position)
path_dijkstra = dijkstra.dijkstra(graph, ini, goal)
path_bellman_ford = bellman_ford.bellmanFord(graph, ini, goal)

# Ejecutar Kruskal y Prim
mst_kruskal, total_cost_kruskal = kruskal.kruskal(graph)
mst_prim, total_cost_prim = prim.prim(graph, ini)

# Menú
opcion = ""
while opcion != "7":
    print("\nMenú de opciones:")
    print("1. A*")
    print("2. Greedy")
    print("3. Dijkstra")
    print("4. Bellman-Ford")
    print("5. Kruskal (MST)")
    print("6. Prim (MST)")
    print("7. Salir")

    opcion = input("Ingrese la opción deseada: ").upper()

    if opcion == "1":
        show.draw(path_aStar)  # Mostrar camino de A*
    elif opcion == "2":
        show.draw(path_best)  # Mostrar camino de Greedy
    elif opcion == "3":
        show.draw(path_dijkstra)  # Mostrar camino de Dijkstra
    elif opcion == "4":
        show.draw(path_bellman_ford)  # Mostrar camino de Bellman-Ford
    elif opcion == "5":
        show.draw_mst(mst_kruskal)  # Mostrar MST de Kruskal
    elif opcion == "6":
        show.draw_mst(mst_prim)  # Mostrar MST de Prim
    elif opcion == "7":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción inválida.")
