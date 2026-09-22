# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class Sensor:
    """Represents a sensor that monitors a value and reports when it goes out of range."""

    def __init__(self, minimum=0, maximum=100, currentValue=0, interval=1, location="Unknown", type="Generic", id=0):
        """Creates a Sensor with default or given minimum, maximum, currentValue, interval, location, type, and id."""
        self.minimum = minimum
        self.maximum = maximum
        self.currentValue = currentValue
        self.interval = interval
        self.location = location
        self.type = type
        self.id = id

    def getMinimum(self):
        return self.minimum

    def setMinimum(self, minimum):
        self.minimum = minimum

    def getMaximum(self):
        return self.maximum

    def setMaximum(self, maximum):
        self.maximum = maximum

    def getCurrentValue(self):
        return self.currentValue

    def setCurrentValue(self, currentValue):
        self.currentValue = currentValue

    def getInterval(self):
        return self.interval

    def setInterval(self, interval):
        self.interval = interval

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def trip(self):
        """Returns True if currentValue is less than minimum or greater than maximum, False otherwise."""
        return self.currentValue < self.minimum or self.currentValue > self.maximum

    def __str__(self):
        return ("minimum: " + str(self.minimum) +
                ", maximum: " + str(self.maximum) +
                ", currentValue: " + str(self.currentValue) +
                ", interval: " + str(self.interval) +
                ", location: " + str(self.location) +
                ", type: " + str(self.type) +
                ", id: " + str(self.id))
