import random
import arrays
class bus(object):
    def __init__(self, number_of_bus, number_of_stops):
        self.number_of_bus = int(number_of_bus)
        #self.connected_stops = []
        self.connected_stops_dict = []
        self.stops = []
        self.stops_dict = {}
        self.hours = {}

        #tworzenie macierzy
        for index in range(int(number_of_stops)):
            self.connected_stops_dict.append([0]*number_of_stops)

    def create_matrix(self):
        for index in range(len(self.connected_stops_dict)):
            for index2 in range(len(self.connected_stops_dict[index])):
                if index == index2:
                    pass
                elif abs(index - index2) == 1:
                    pass
                elif index < index2:
                    sumUp = self.connected_stops_dict[index][index2-1] + self.connected_stops_dict[index2-1][index2]
                    self.connected_stops_dict[index][index2] = sumUp



    def add_stop_dict(self, stopName, direction):
        self.stops_dict[direction] = stopName

    def add_connection_between_stops(self, direction):
        for stop in range(1, len(self.stops_dict[direction])):
            time = random.randint(1, 3)
            self.connected_stops_dict[stop][stop - 1] = time
            self.connected_stops_dict[stop - 1][stop] = time


    def add_hours_dict(self, stopName, hour, direction):
        self.hours[direction] = [hour]

    def calculate_next_stops_hours(self):
        for index in range(0, len(self.stops_dict[1]) - 1):
            timeBeetwenStops = self.connected_stops_dict[index][index+1]
            for index2 in range(0, len(self.hours[1])):
                listOfHours = []
                for index3 in range(0, len(self.hours[1][index2])):
                    hour = self.hours[1][index2][index3][0]
                    minute = self.hours[1][index2][index3][1]
                    minute += timeBeetwenStops
                    while (minute > 59):
                        minute -= 60
                        hour += 1
                    listOfHours.append([hour, minute])
            self.hours[1].append(listOfHours)

    def calculate_next_stops_hours_second_direction(self):
        for index in range(len(self.stops_dict[2]) -1, 0, -1): #poziom busa
            timeBeetwenStops = self.connected_stops_dict[index][index-1]
            for index2 in range(0, len(self.hours[2])): #poziom przystanku
                listOfHours = []
                for index3 in range(0, len(self.hours[2][index2])): #poziom pojedynczego odjazdu
                    hour = self.hours[2][index2][index3][0]
                    minute = self.hours[2][index2][index3][1]
                    minute += timeBeetwenStops
                    while (minute > 59):
                        minute -= 60
                        hour += 1
                    listOfHours.append([hour, minute])
            self.hours[2].append(listOfHours)


    def get_hours(self, stopName, direction):
        index = self.get_id_of_stop_dict(stopName, direction)
        for hour in self.hours[direction][index]:
            print(hour[0], ":", hour[1])    #hour[0] -> godzina  ;  hour[1] -> minuta

    def return_hours(self, stopName, direction):
        index = self.get_id_of_stop_dict(stopName, direction)
        return self.hours[direction][index]

    def get_name_of_stop_dict(self, index, direction):
        return self.stops_dict[direction][index]

    def get_id_of_stop_dict(self, stopName, direction):
        return ((self.stops_dict[direction]).index(stopName))

    def get_stops_dict(self, direction):
        return self.stops_dict[direction]

    def get_connected_stops(self):
        return self.connected_stops_dict

    def get_time_between_stops_algorithm(self, firstStation, lastStation, direction):
        firstIndex = self.get_id_of_stop_dict(firstStation, direction)
        secondIndex = self.get_id_of_stop_dict(lastStation, direction)
        if direction == 1:
            return self.connected_stops_dict[firstIndex][secondIndex]
        else:
            length = len(self.connected_stops_dict)-1
            return self.connected_stops_dict[length-secondIndex][length-firstIndex]






