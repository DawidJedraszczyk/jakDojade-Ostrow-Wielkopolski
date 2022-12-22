import graph
import bubble

def algorithm(firstStation, lastStation, hour, minute, maxTime, graph):
    busesListFirstStop = graph.get_other_buses_from_same_stop(firstStation)
    busesListLastStop = graph.get_other_buses_from_same_stop(lastStation)
    solutions = []

    def checkIfThereIsTheSameBus(busList):
        listOfBuses = []
        for busName in busList:
            if busName in busesListLastStop:
                listOfBuses.append(busName)
        return listOfBuses

    def checkDirection(busName, startStation, goalStation):
        firstDirection = graph.get_stops_dict(busName, 1)

        if firstDirection.index(startStation) < firstDirection.index(goalStation):
            return 1
        else:
            return 2

    def checkDepartureHours(busName, firstStation, direction, setMinHour, setMinMinute):
        firstStationDepartureHours = graph.return_hours(busName, firstStation, direction)

        firstStationHour = 0
        firstStationMinute = 0

        for clock in firstStationDepartureHours:
            firstStationHour = clock[0]
            firstStationMinute = clock[1]
            if (firstStationHour > setMinHour or (firstStationHour == setMinHour and firstStationMinute >= setMinMinute)):
                break
        return firstStationHour, firstStationMinute

    def checkOverflow(checkHour, checkMinute):
        if checkMinute > 59:
            checkHour += 1
            checkMinute -= 60
        return checkHour, checkMinute

    def sumUpTravelTime(lastStationHour, lastStationMinute, firstStationHour, firstStationMinute):
        if lastStationMinute > firstStationMinute and lastStationHour > firstStationHour:
            return lastStationHour-firstStationHour, lastStationMinute-firstStationMinute
        elif lastStationMinute > firstStationMinute and lastStationHour == firstStationHour:
            return 0, lastStationMinute-firstStationMinute
        elif lastStationMinute < firstStationMinute and lastStationHour > firstStationHour:
            return lastStationHour-1-firstStationHour, lastStationMinute+60-firstStationMinute
        elif lastStationMinute == firstStationMinute and lastStationHour > firstStationHour:
            return lastStationHour-firstStationHour, 0


        #   przypadek gdy nie potrzeba się przesiadać
    firstTransportOption = checkIfThereIsTheSameBus(busesListFirstStop)

    for option in firstTransportOption:     #tutaj przejście po możliwych do wyboru dojazdach
        direction = checkDirection(option, firstStation, lastStation)
        hour2 = hour
        minute2 = minute
        solutionsFound = 0
        while solutionsFound < 20:
            firstStationHour, firstStationMinute = checkDepartureHours(option, firstStation, direction, hour2, minute2)

            time = graph.get_time_between_stops_algorithm(firstStation, lastStation, option, direction)
            if time:
                addedHour = time // 60
                addedMinute = time - addedHour*60

                lastStationHour = firstStationHour + addedHour
                lastStationMinute = firstStationMinute + addedMinute
                if lastStationMinute > 59:
                    lastStationHour += 1
                    lastStationMinute -= 60
                travelTimeHour, travelTimeMinute = sumUpTravelTime(lastStationHour, lastStationMinute, firstStationHour, firstStationMinute)
                solution = [option, None, None, None, None, [travelTimeHour, travelTimeMinute],[firstStationHour, firstStationMinute],[None,None],[None, None], [None, None], [None, None], [lastStationHour, lastStationMinute]]
                if solution not in solutions:
                    solutions.append(solution)
            solutionsFound += 1
            minute2 += 10
            if minute2 > 59:
                hour2 += 1
                minute2 -= 60

            #   przypadek z przesiadką
            #   1 przesiadka

    for busName in busesListFirstStop:          #przejscie po kazdym z busow na pierwszym przystanku          #przejscie po kazdym kierunku jazdy
        stopsList = graph.get_stops_dict(busName, 1)        #lista przystankow
        for secondStopName in stopsList:
            if secondStopName != firstStation and secondStopName != lastStation:        #brało losowego busa z tej stacji, zeby dojechac na tę samą stację i pojechać bezpośrednio
                firstBusDirection = checkDirection(busName, firstStation, secondStopName)
                busList = graph.get_other_buses_from_same_stop(secondStopName)
                secondOption = checkIfThereIsTheSameBus(busList)
                firstStationHour, firstStationMinute = checkDepartureHours(busName, firstStation, firstBusDirection, hour,minute)
                timeBetween = graph.get_time_between_stops_algorithm(firstStation, secondStopName, busName, firstBusDirection)
                tmpHour = firstStationHour + timeBetween // 60
                tmpMinute = firstStationMinute + timeBetween % 60
                secondStationHourArrival, secondStationMinuteArrival = checkDepartureHours(busName, secondStopName,firstBusDirection, tmpHour,tmpMinute)
                minSecondStationMinuteDeparture = secondStationMinuteArrival + 3  # doliczamy 3 minuty na przesiadkę
                minSecondStationHourDeparture = secondStationHourArrival
                if minSecondStationMinuteDeparture > 59:
                    minSecondStationMinuteDeparture -= 60
                    minSecondStationHourDeparture += 1
                for secondBus in secondOption:
                    if secondBus != busName:
                        secondBusDirection = checkDirection(secondBus, secondStopName, lastStation)
                        secondStationHourDeparture, secondStationMinuteDeparture = checkDepartureHours(secondBus, secondStopName, secondBusDirection, minSecondStationHourDeparture, minSecondStationMinuteDeparture)
                        timeBetween = graph.get_time_between_stops_algorithm(secondStopName, lastStation, secondBus, secondBusDirection)
                        tmpHour = secondStationHourDeparture + timeBetween // 60
                        tmpMinute = secondStationMinuteDeparture + timeBetween % 60
                        lastStationHourArrival, lastStationMinuteArrival = checkDepartureHours(secondBus, lastStation, secondBusDirection, tmpHour, tmpMinute)
                        travelTimeHour, travelTimeMinute = sumUpTravelTime(lastStationHourArrival, lastStationMinuteArrival, firstStationHour, firstStationMinute)

                        solutions.append([busName, secondBus, secondStopName, None, None, [travelTimeHour, travelTimeMinute],[firstStationHour, firstStationMinute],[secondStationHourArrival,secondStationMinuteArrival],[secondStationHourDeparture, secondStationMinuteDeparture], [None, None], [None, None], [lastStationHourArrival, lastStationMinuteArrival]])
                #if not secondOption:
                #    for secondBusName in busList:           # PIERWSZA PRZESIADKA
                #        if secondBusName != busName:
                #            stopsList = graph.get_stops_dict(secondBusName, 1)
                #            for thirdStopName in stopsList:
                #                if thirdStopName != firstStation and thirdStopName != lastStation and thirdStopName != secondStopName:
                #                    secondBusDirection = checkDirection(secondBusName, secondStopName, thirdStopName)
                #                    secondStationHourDeparture, secondStationMinuteDeparture = checkDepartureHours(secondBusName, secondStopName, secondBusDirection, minSecondStationHourDeparture, minSecondStationMinuteDeparture)
                #                    timeBetween = graph.get_time_between_stops_algorithm(secondStopName, thirdStopName,secondBusName, secondBusDirection)
                #                    tmpHour = secondStationHourDeparture + timeBetween // 60
                #                    tmpMinute = secondStationMinuteDeparture + timeBetween % 60
                #                    thirdStationHourArrival, thirdStationMinuteArrival = checkDepartureHours(secondBusName, thirdStopName, secondBusDirection, tmpHour, tmpMinute)
                #                    thirdStopBusList = graph.get_other_buses_from_same_stop(thirdStopName)
                #                    thirdOption = checkIfThereIsTheSameBus(thirdStopBusList)
                #                    minThirdStationMinuteDeparture = thirdStationMinuteArrival + 3  # doliczamy 3 minuty na przesiadkę
                #                    minThirdStationHourDeparture = thirdStationHourArrival
                #                    if minThirdStationMinuteDeparture > 59:
                #                        minThirdStationMinuteDeparture -= 60
                #                        minThirdStationHourDeparture += 1
                #                    if thirdOption and thirdOption!= secondBusName:             # DRUGA PRZESIADKA
                #                        for thirdBus in thirdOption:
                #                            thirdBusDirection = checkDirection(thirdBus, thirdStopName, lastStation)
                #                            thirdStationHourDeparture, thirdStationMinuteDeparture = checkDepartureHours(thirdBus, thirdStopName, thirdBusDirection,minThirdStationHourDeparture, minThirdStationMinuteDeparture)
                #                            timeBetween = graph.get_time_between_stops_algorithm(thirdStopName,lastStation,thirdBus,thirdBusDirection)
                #                            tmpHour = thirdStationHourDeparture + timeBetween // 60
                #                            tmpMinute = thirdStationMinuteDeparture + timeBetween % 60
                #                            lastStationHourArrival, lastStationMinuteArrival = checkDepartureHours(thirdBus, lastStation, thirdBusDirection, tmpHour, tmpMinute)
                #                            travelTimeHour, travelTimeMinute = sumUpTravelTime(lastStationHourArrival, lastStationMinuteArrival, firstStationHour, firstStationMinute)
                #                            solutions.append([busName, secondBusName, secondStopName, thirdBus, thirdStopName, [travelTimeHour, travelTimeMinute],[firstStationHour, firstStationMinute],[secondStationHourArrival,secondStationMinuteArrival],[secondStationHourDeparture, secondStationMinuteDeparture], [thirdStationHourArrival, thirdStationMinuteArrival], [thirdStationHourDeparture, thirdStationMinuteDeparture], [lastStationHourArrival, lastStationMinuteArrival]])

    bubble.bubbleSort(solutions)
    for index in solutions:
        print(index)
