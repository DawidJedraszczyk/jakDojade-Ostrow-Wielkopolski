import math
import json
import networkx as nx
import matplotlib.pyplot as plt

with open('sprawozdanieAddBusList.json', 'r') as file:
    busesArr = json.load(file)

with open('sprawozdanieAddStopsList.json', 'r', encoding='utf8') as file2:
    stopsArr = json.load(file2)
allStations = []
visual = []
busNames = ['busNr1', 'busNr2', 'busNr4', 'busNr5', 'busNr6']

for bus in range(len(busesArr['buses'])):
    busName = busNames[bus]
    for station in range(1, len(stopsArr['stopsList'][bus][busName])):
        first = stopsArr['stopsList'][bus][busName][station-1]
        second = stopsArr['stopsList'][bus][busName][station]
        print(first,second)
        visual.append([first, second])
        #print(first, second)
        if first not in allStations:
            allStations.append(first)
        if second not in allStations:
            allStations.append(second)

ostrowGraph = nx.Graph()
ostrowGraph.add_edges_from(visual)
nx.draw(ostrowGraph, with_labels=True)
plt.show()

#for station in allStations:
#    print(station)