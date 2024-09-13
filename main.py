from algorithm import aStar, best, neighbors
from static import show
ini = 'Tauramena'
goal = 'Bogotá'
graph = neighbors.getGraph()
path = aStar.aStar(graph,ini,goal,neighbors.getPosition())

show.draw()

if path:
    print("Path A* found:", path)
else:
    print("No path found between", ini, "and", goal)

path = best.greedyBestFirstSearch(graph,ini,goal,neighbors.getPosition())

if path:
    print("Path Greedy found:", path)
else:
    print("No path found between", ini, "and", goal)   
    
