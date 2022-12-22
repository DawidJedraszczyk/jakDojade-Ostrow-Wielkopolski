import graph

def algorithm(firstStation, lastStation, hour, minute, maxTime, graph):
    print("trasa ", firstStation, " ==> ", lastStation)
    busesListFirstStop = graph.get_other_buses_from_same_stop(firstStation)
    busesListLastStop = graph.get_other_buses_from_same_stop(lastStation)
    optionCounter = 0

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
                # print(firstStationHour, ":", firstStationMinute)
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
    if firstTransportOption:
        optionCounter = 1
    theFastestOption = ["busName", maxTime, [25, 61], [25, 61]]             # [busName, travelTime, startTime, onPlaceTime]
    firstOnPlaceOption = ["busName", maxTime, [25, 61], [25, 61]]


    for option in firstTransportOption:     #tutaj przejście po możliwych do wyboru dojazdach
        direction = checkDirection(option, firstStation, lastStation)

        firstStationHour, firstStationMinute = checkDepartureHours(option, firstStation, direction, hour, minute)

        time = graph.get_time_between_stops_algorithm(firstStation, lastStation, option, direction)
        #print(time)
        if time < maxTime:
            addedHour = time // 60
            addedMinute = time - addedHour*60

            lastStationHour = firstStationHour + addedHour
            lastStationMinute = firstStationMinute + addedMinute
            if lastStationMinute > 59:
                lastStationHour += 1
                lastStationMinute -= 60
            #print("Na przystanku będziesz o:")
            #print(lastStationHour, ":", lastStationMinute)

            if (lastStationHour <=  firstOnPlaceOption[3][0] and lastStationMinute < firstOnPlaceOption[3][1]):
                firstOnPlaceOption = [option, time, [firstStationHour, firstStationMinute], [lastStationHour, lastStationMinute]]

            if time < theFastestOption[1]:
                theFastestOption = [option, time, [firstStationHour, firstStationMinute], [lastStationHour, lastStationMinute]]

    if optionCounter == 1:
        print("Jedziesz bezposrednio \n")
        print("najkrotsza jazda: ")
        print("-> Wsiądź do", theFastestOption[0], "trasa będzie trwała", theFastestOption[1], " minuty \n-->wyjazd z przystanku ", firstStation, "o godzinie", theFastestOption[2][0], ":", theFastestOption[2][1], "\n--->na miejscu będziesz o godzinie:", theFastestOption[3][0], ":", theFastestOption[3][1])
        print("")
        print("najszybciej na miejscu")
        print("-> Wsiądź do", firstOnPlaceOption[0], "trasa będzie trwała", firstOnPlaceOption[1], "minuty \n-->wyjazd z przystanku ", firstStation, "o godzinie", firstOnPlaceOption[2][0], ":", firstOnPlaceOption[2][1], "\n--->na miejscu będziesz o godzinie:", firstOnPlaceOption[3][0], ":", firstOnPlaceOption[3][1])
        print("")
        print("")

        #   przypadek z przesiadką

            #   1 przesiadka


    theFastestSecondOption = ["busName", "secondBusName", "secondStationName" , [25, 61], [25, 61], [25, 61], [25, 61], [25, 61], [25, 61]]                  # [busName, secondbus, secondstation, travelTime, startTime, firstStationTime, secondStationArrival, SecondStationDeportureTime, onPlaceTime]
    firstOnPlaceSecondOption = ["busName", "secondBusName","secondStationName", [25, 61], [25, 61], [25, 61], [25, 61], [25, 61], [25, 61]]

    #if optionCounter < 1:
    for busName in busesListFirstStop:          #przejscie po kazdym z busow na pierwszym przystanku
        for direction in range(1, 3):           #przejscie po kazdym kierunku jazdy
            stopsList = graph.get_stops_dict(busName, direction)        #lista przystankow
            for secondStopName in stopsList:
                if secondStopName != firstStation:        #brało losowego busa z tej stacji, zeby dojechac na tę samą stację i pojechać bezpośrednio
                    busList = graph.get_other_buses_from_same_stop(secondStopName)
                    secondOption = checkIfThereIsTheSameBus(busList)
                    if secondOption != busName:
                        optionCounter = 2
                        firstStationHour, firstStationMinute = checkDepartureHours(busName, firstStation, direction, hour, minute)
                        timeBetween = graph.get_time_between_stops_algorithm(firstStation, secondStopName, busName, direction)
                        tmpHour = firstStationHour + timeBetween//60
                        tmpMinute = firstStationMinute + timeBetween%60
                        secondStationHourArrival, secondStationMinuteArrival = checkDepartureHours(busName, secondStopName, direction, tmpHour, tmpMinute)
                        minSecondStationMinuteDeparture = secondStationMinuteArrival + 3 # doliczamy 3 minuty na przesiadkę
                        minSecondStationHourDeparture = secondStationHourArrival
                        if minSecondStationMinuteDeparture > 59:
                            minSecondStationMinuteDeparture -= 60
                            minSecondStationHourDeparture += 1
                        for secondBus in secondOption:
                            if secondBus != busName:
                                secondBusDirection = checkDirection(secondBus, secondStopName, lastStation)
                                secondStationHourDeparture, secondStationMinuteDeparture = checkDepartureHours(secondBus, secondStopName, secondBusDirection, minSecondStationHourDeparture, minSecondStationMinuteDeparture)

                                lastStationHourArrival, lastStationMinuteArrival = checkDepartureHours(secondBus, lastStation, secondBusDirection, secondStationHourDeparture, secondStationMinuteDeparture)

                                travelTimeHour, travelTimeMinute = sumUpTravelTime(lastStationHourArrival, lastStationMinuteArrival, firstStationHour, firstStationMinute)

                                if ((travelTimeHour <= theFastestSecondOption[3][0] and travelTimeMinute < theFastestSecondOption[3][1]) or (travelTimeHour < theFastestSecondOption[3][0])):
                                    theFastestSecondOption = [busName, secondBus, secondStopName, [travelTimeHour, travelTimeMinute], [firstStationHour, firstStationMinute], [secondStationHourArrival, secondStationMinuteArrival], [secondStationHourDeparture, secondStationMinuteDeparture], [lastStationHourArrival, lastStationMinuteArrival]]

                                if ((lastStationHourArrival <= firstOnPlaceSecondOption[7][0] and lastStationMinuteArrival < firstOnPlaceSecondOption[7][1]) or (lastStationHourArrival < firstOnPlaceSecondOption[7][0])):
                                    firstOnPlaceSecondOption = [busName, secondBus, secondStopName, [travelTimeHour, travelTimeMinute], [firstStationHour, firstStationMinute], [secondStationHourArrival, secondStationMinuteArrival],[secondStationHourDeparture, secondStationMinuteDeparture], [lastStationHourArrival, lastStationMinuteArrival]]
    if optionCounter == 2:
        print("jedziesz z 1 przesiadką \n")
        print("najszybciej na miejscu będzie: ")
        print(" -> wsiadz do busa", firstOnPlaceSecondOption[0], "na przystanku", firstStation, "o godzinie:", firstOnPlaceSecondOption[4][0], ":", firstOnPlaceSecondOption[4][1])
        print(" --> wysiądź na przystanku", firstOnPlaceSecondOption[2], "o godzinie:", firstOnPlaceSecondOption[5][0], ":", firstOnPlaceSecondOption[5][1])
        print(" ---> przesiadka na przystanku", firstOnPlaceSecondOption[2], "do", firstOnPlaceSecondOption[1], "o godzinie:", firstOnPlaceSecondOption[6][0], ":", firstOnPlaceSecondOption[6][1])
        print(" ----> na przystanku docelowym będziesz o godzinie:", firstOnPlaceSecondOption[7][0], ":", firstOnPlaceSecondOption[7][1])
        print(" -----> trasa będzie łącznie trwała:", firstOnPlaceSecondOption[3][0], ":", firstOnPlaceSecondOption[3][1])
        print("")
        print("najkrócej jedzie: ")
        print(" -> wsiadz do busa", theFastestSecondOption[0], "na przystanku", firstStation, "o godzinie:", theFastestSecondOption[4][0], ":", theFastestSecondOption[4][1])
        print(" --> wysiądź na przystanku", theFastestSecondOption[2], "o godzinie:", theFastestSecondOption[5][0], ":", theFastestSecondOption[5][1])
        print(" ---> przesiadka na przystanku", theFastestSecondOption[2], "do", theFastestSecondOption[1], "o godzinie:", theFastestSecondOption[6][0], ":", theFastestSecondOption[6][1])
        print(" ----> na przystanku docelowym będziesz o godzinie:", theFastestSecondOption[7][0], ":", theFastestSecondOption[7][1])
        print(" -----> trasa będzie łącznie trwała:", theFastestSecondOption[3][0], ":", theFastestSecondOption[3][1])
        print("")
