import algorithm
import graph
import arrays
import random
import json

#parsing json

#   !!!!!!!!!!!     aby sprawdzić działanie dla pełnych danych wystarczy zmienić 'sprawozdanieAddBusList.json' <=> 'addBusList.json' oraz 'sprawozdanieAddStopsList.json' <=> 'addStopsList.json' i odwrotnie
#   !!!!!!!!!!!         tę samą operację trzeba wykonać w pliku graph

with open('addBusList.json', 'r') as file:
    busesArr = json.load(file)

with open('addStopsList.json', 'r', encoding='utf8') as file2:
    stopsArr = json.load(file2)
#creating city graph -> Graph(numberOfBusesInCity)

ostrow = graph.Graph(2)


#adding buses  -> add_bus(busName, numberOfBus, numberOfStops)

for index in range(len(busesArr['buses'])):
    #print(busesArr['buses'][index])
    busName = busesArr['buses'][index]['busName']
    busNumber = busesArr['buses'][index]['busNumber']
    numberOfStops = busesArr['buses'][index]['numberOfStops']
    ostrow.add_bus(busName, busNumber, numberOfStops)

##adding stops -> add_stop(busName, stopName)

for busNumber in range(len(stopsArr['stopsList'])):
    busName = busesArr['buses'][busNumber]['busName']
    lastIndex = len(stopsArr['stopsList'][busNumber][busName])-1
    ostrow.add_stop_dict(busName, stopsArr['stopsList'][busNumber][busName], 1)
    tmp = []
    for index in range(len(stopsArr['stopsList'][busNumber][busName])-1, -1, -1):
        tmp.append(stopsArr['stopsList'][busNumber][busName][index])
    ostrow.add_stop_dict(busName, tmp, 2)


##adding connection between stops -> add_connection_between_stops(busName, stop1, stop2, timeBetween(in Min) )
for busNumber in range(len(busesArr['buses'])):
    busName = busesArr['buses'][busNumber]['busName']
    ostrow.add_connection_between_stops_dict(busName, 1)

    #generating
for index in range(len(busesArr['buses'])):
    busName = busesArr['buses'][index]['busName']
    firstStation = stopsArr['stopsList'][index][busName][0]
    tmp = []
    hourOfStart = 6
    for index2 in range(14):
        hour = hourOfStart
        minute = random.randint(0, 59)
        tmp.append([hour, minute])
        hourOfStart += 1
    ostrow.add_hour_dict(busName, firstStation, tmp, 1)

for index in range(len(busesArr['buses'])):
    busName = busesArr['buses'][index]['busName']
    lastIndex = len(stopsArr['stopsList'][index][busName])-1
    firstStationSecondDirection = stopsArr['stopsList'][index][busName][lastIndex]
    tmp = []
    hourOfStart = 6
    for index2 in range(14):
        hour = hourOfStart
        minute = random.randint(0, 59)
        tmp.append([hour, minute])
        hourOfStart += 1
    ostrow.add_hour_dict(busName, firstStationSecondDirection, tmp, 2)

##calculating hours of stops
for index in range(len(busesArr['buses'])):
    busName = busesArr['buses'][index]['busName']

    #ostrow.calculate_next_stops_hours_second_direction(busName)
    ostrow.calculate_next_stops_hours(busName)

#       MAIN


algorithm.algorithm('Centrum przesiadkowe', 'Odolanowska I', 15, 36, 100, ostrow)
#ostrow.get_connected_stops("busNr2")


    #TODO
#print(ostrow.get_name_of_stop_dict('busNr1', 1, 2))

#print(ostrow.get_outgoing_stops_without_bus_name("Gorzycka Swobodna", 1))


#while(True):
#    print('''Wybierz:
#    1. lista busow
#    2. lista przystankow
#    3. lista polaczonych przystankow (czas między nimi)
#    5. godziny odjazdu
#    6. wyszukanie trasy
#    10. koniec''')

#    choose = int(input())
    #choose = 6

#    if choose == 1:
    ##getting the buses
#        print( "", *ostrow.get_buses(), sep="       bus nr")
#    elif choose == 2:
    ##getting the stops
#        print("Trasę którego busa chcesz poznać (format -> busNr1, busNr2, itd)")
#        choose2 = input()
        #print(' -> '.join(ostrow.get_stops(choose2)))
#        print(' -> '.join(ostrow.get_stops_dict(choose2, 1)))
#        print("")
#        print(' -> '.join(ostrow.get_stops_dict(choose2, 2)))
#        print("")
#    elif choose == 3:
#        print("Trasę którego busa chcesz poznać (format -> busNr1, busNr2, itd)")
#        choose2 = input()
#        ostrow.get_connected_stops(choose2)
#    elif choose == 5:
#        print("Z jakiego przystanku sprawdzic godziny odjazdu:")
#        choose2 = input()
#        print("Jaki autobus nas interesuje:")
#        choose3 = input()
#        print("W którym kierunku mamy jechać?")
#        choose4 = int(input())
#        print(choose3, " z przystanku ", choose2, " odjezdza o godzinach :")

#        ostrow.get_hours(choose3, choose2, choose4)
#    elif choose == 6:
        #print("Z jakiego przystanku startujemy?")
        #firstStop = input()
        #print("Jaki przystanek jest docelowy?")
        #goalStop = input()
        #print("O której godzinie wyruszamy?")
        #hour, minute = input().split(":")
        #print("Ile czasu maksymalnie może zająć podróż? (w minutach)")
        #maxTime = int(input())


        #algorithm.algorithm(firstStop, goalStop, hour, minute, maxTime, ostrow)


#    elif choose == 10:
#        break

