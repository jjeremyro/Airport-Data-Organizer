from Flight import *
from Airport import *

allAirports = [] # list that contains all Airport objects
allFlights = {} # dictionary that contains all Flight objects

def loadData(airportFile, flightFile):

    try: # to make sure that correct files are used
        airportFile = open(airportFile, "r")
        flightFile = open(flightFile, "r")

    except IOError:
        return False

    for eachLine in airportFile: # loop goes through each line in flightInfo
        eachLine = eachLine.strip() # strips the space of the ends of each side of the line
        eachLine = eachLine.split(",") # splits the elements in the line by commas and puts them into a list
        eachLine = [element.strip() for element in eachLine] # each element has its blank spaces striped from either side
        city = eachLine[1]
        eachLine[1] = eachLine[2]
        eachLine[2] = city
        allAirports.append(eachLine) # adds eachLine (airport code, country, city) to the allAirports container

    # allFlights dictionary is initialized
    for i in range(len(allAirports)): # loops through n number of elements in allAirports
        airportCode = allAirports[i][0]
        allFlights[str(airportCode)] = [] # assigning an instance of the airportCode as a key to an empty list so that we can later add the flight objects

    # cleaning up / formatting flights.txt
    for eachLine in flightFile: # loop goes through each line in flightInfo
        eachLine = eachLine.strip()
        eachLine = eachLine.split(",") #
        eachLine = [element.strip() for element in eachLine] # strips the spaces off either side of each element, then adds them into a list
        flightNo = eachLine[0] # assigning each index in the list to different variables
        originCode = eachLine[1]
        destinationCode = eachLine[2]

        # origin and destination object
        originObject = getAirportByCode(originCode) # refers to getAirportByCode function to create originObject
        destinationObject = getAirportByCode(destinationCode) # refers to getAirportByCode function to create destinationObject

        # flight object
        flightObject = Flight(flightNo, originObject, destinationObject)
        allFlights[originCode].append(flightObject) # adds all flightObjects into the allFlights dictionary

    return True

# takes the origin code as an argument and returns airportObject
def getAirportByCode(originCode):
    for i in range(len(allAirports)): # loops through the number of elements in the allAirports list
        if originCode == str(allAirports[i][0]): # if the originCode is the same as the instance originCode from allAirports...
            airportObject = Airport(allAirports[i][0], allAirports[i][1], allAirports[i][2]) # creates an airport object
            return airportObject

    return -1 # if originCode isn't equal to the instance origin code, -1 is returned

def findAllCityFlights(city):
    cityFlightsList = [] # This list contains all the flights from and to a particular city

    for eachLine in range(145): # loops 146 times (represents the number of lines in the flights.txt file)

        for eachFlight in allFlights: # loops through each flight in the allFlights dictionary
            allFlightsList = allFlights[eachFlight] # each flight in the dictionary is added to a list
            numberOfFlights = len(allFlightsList)


            for i in range(numberOfFlights): # loops through the length of allFlightsList
                if city in str(allFlightsList[i]): # if the city that is specified is in the instance of allFlightsList...
                    cityFlightsList.append(allFlightsList[i]) # added to the cityFlightsList

        return cityFlightsList

def findAllCountryFlights(country):

    sameCountryList = [] # This list contains the geographical locations airports from the same country
    sameCountryFlights = [] # This list contains all the flights from and to a particular country

    for line in range(36): # this loop will run 37 times
        if country == allAirports[line][2]: # if the country is the same as the country in allAirports at this specific instance...
            sameCountryList.append(allAirports[line]) # it will add the geographical location of the airport in the sameCountry list

    for cities in sameCountryList: # this will loop through each index in sameCountryList
        for i in allFlights: # nested for loop to go through each index in allFlights
            allFlightsList = allFlights[i] # assigns allFlightsList variable the element with the same country as the ones in sameCountryList
            numberOfFlights = len(allFlightsList)

            for index in range(numberOfFlights): # another nested for loop that goes through n number of Flights there are in allFlightslist
                individualFlight = allFlightsList[index] # assigns individualFlights each index of allFlightsList as it goes through the loop
                city = cities[1]
                if city in str(individualFlight): # if the specific city is found in individualFlight...
                    sameCountryFlights.append(individualFlight) # adds the whole flight (individualFlight) to the sameCountryFlights list

    return sameCountryFlights

def findFlightBetween(origin, destination):
    stopList = []
    finalDestination = destination.getCity() # using getCity() function from airport file to get city
    finalDestinationCode = destination.getCode() # using getCountry() function from airport file to get country
    OriginCode = origin.getCode() # using getCode() function from airport file to get code

    flightFromOrigin = allFlights[OriginCode] # finds if there is a direct flight or not

    for i in range(len(flightFromOrigin)): # loops through the number of elements in flightFromOrigin dictionary
        if finalDestination in str(flightFromOrigin[i]): # if the final destination is in the instance of flightFromOrigin, returns statement
            return "Direct Flight: " + OriginCode + " to " + finalDestinationCode

    for individualFlight in flightFromOrigin: # loop adds destination code to the list, if direct flight isn't found
        stopList.append(individualFlight.getDestination().getCode())

    halfwayCodes = set()

    index = 0
    while index < len(stopList): # this while loop loops until index becomes equal to, or bigger than stopList length
        flightsHalfway = allFlights[stopList[index]]
        for flight in flightsHalfway:
            if finalDestination in str(flight): # if a destination is found, this adds halfway code to set
                halfwayCodes.add(stopList[index])
        index += 1

    if len(halfwayCodes) != 0: # checks for single hop flights
        return halfwayCodes
    else:
        return -1

