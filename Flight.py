from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        if isinstance(origin,Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("the origin and destination must be airport objects")

    def __repr__(self):
        if self.isDomesticFlight() == True:
            return "Flight:" + " " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {domestic}"
        elif self.isDomesticFlight() == False:
            return "Flight:" + " " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {international}"

    def __eq__(self, other):
        return self._destination == other._destination and self._origin == other._origin

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        #print(self._origin)
        if self._origin.getCountry() == self._destination.getCountry():
            #print("True")
            return True
        else:
            #print("False")
            return False

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination