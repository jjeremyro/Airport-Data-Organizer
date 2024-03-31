class Airport: # Class Airport that will help construct airport and light object in Assign4 file
    def __init__(self, code, city, country): #intializes the variables/arguments
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self): # formats code, city, and country into required format
        return self._code + " (" + self._city + ", " + self._country + ")"

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country