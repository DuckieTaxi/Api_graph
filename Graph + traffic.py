import copy
import networkx as nx 
import matplotlib.pyplot as plt 

DG = nx.Graph()
DG.add_edge('S', 'a')
DG.add_edge('a', 'b')
DG.add_edge('a', 'c')
DG.add_edge('b', 'd')
DG.add_edge('b', 'e')
DG.add_edge('c', 'e')
DG.add_edge('c', 'f')
DG.add_edge('d', 'T')
DG.add_edge('e', 'T')
DG.add_edge('f', 'T')


remove = []
a = input("введите начало пробки")
b = input("введите конец пробки")

ways = [p for p in nx.all_shortest_paths(DG, source='S', target='T')]
ways_c = copy.deepcopy(ways)

print(ways)

for i in range(0, len(ways_c)-1):
    for j in range(0, len(ways_c[i])):
        if ways[i][j] == a and ways[i][j+1] == b:
            ways.pop(i)

print(ways)
# nx.draw_networkx(DG)

# plt.show()