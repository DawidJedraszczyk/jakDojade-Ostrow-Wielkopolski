import arrays
import buses
import json
with open('addBusList.json', 'r') as file:
    busesArr = json.load(file)

class Graph(object):
    def __init__(self, numberOfBuses):
        self.numberOfBuses = numberOfBuses
        self.busesNames = []
        self.busObjects = {}

    def add_bus(self, busName, numberOfBus, numberOfStops):
        self.busesNames.append(numberOfBus)
        bus = buses.bus(numberOfBus, numberOfStops)
        self.busObjects[busName] = bus

    def add_stop_dict(self, busName, stopName, direction):
        self.busObjects[busName].add_stop_dict(stopName, direction)

    def add_connection_between_stops_dict(self, busName, direction):
        self.busObjects[busName].add_connection_between_stops(direction)

    def add_hour_dict(self, busName, stopName, hour, direction):
        self.busObjects[busName].add_hours_dict(stopName, hour, direction)

    def get_other_buses_from_same_stop(self, stopName):
        listOfBuses = []
        for index in range(len(busesArr['buses'])):
            #busName = arrays.addBusList[index][0]
            busName = busesArr['buses'][index]['busName']
            stops1 = self.busObjects[busName].get_stops_dict(1)
            stops2 = self.busObjects[busName].get_stops_dict(2)
            if (stopName in stops1) or (stopName in stops2):
                listOfBuses.append(busName)
        return(listOfBuses)

    def get_hours(self, busName, stopName, direction):
        self.busObjects[busName].get_hours(stopName, direction)

    def return_hours(self, busName, stopName, direction):
        return self.busObjects[busName].return_hours(stopName, direction)


    def get_connected_stops(self, busName):
        matrix = (self.busObjects[busName].get_connected_stops())
        for index in matrix:
            row = []
            for index2 in index:
                row.append(index2)
            print(*row, sep=" ")

    def get_buses(self):
        return self.busesNames

    def get_all_stops(self):
        stops = []
        for index in range(len(arrays.addBusList)):
            busName = arrays.addBusList[index][0]
            stopsTmp1 = self.busObjects[busName].get_stops_dict(1)
            stopsTmp2 = self.busObjects[busName].get_stops_dict(2)
            for index2 in stopsTmp1:
                if index2 not in stops:
                    stops.append(index2)
            for index2 in stopsTmp2:
                if index2 not in stops:
                    stops.append(index2)
        stops.sort()
        return(stops)


    def get_time_between_stops_algorithm(self, firstStation, lastStation, busName, direction):
        return self.busObjects[busName].get_time_between_stops_algorithm(firstStation, lastStation, direction)


    def get_stops_dict(self, busName, direction):
        return self.busObjects[busName].get_stops_dict(direction)

    def calculate_next_stops_hours(self, busName):
        self.busObjects[busName].calculate_next_stops_hours()
        self.busObjects[busName].calculate_next_stops_hours_second_direction()
        self.busObjects[busName].create_matrix()

    def get_name_of_stop_dict(self, busName, index, direction):
        self.busObjects[busName].get_name_of_stop_dict(index, direction)