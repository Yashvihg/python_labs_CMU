# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class Device:
    """Represents a controllable device identified by type, location, and id."""

    def __init__(self, type="Generic", location="Unknown", id=0):
        """Creates a Device with default or given type, location, and id."""
        self.type = type
        self.location = location
        self.id = id

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def actuate(self):
        """Prints the device's formatted data in all caps."""
        print(str(self).upper())

    def __str__(self):
        return "type: " + str(self.type) + ", location: " + str(self.location) + ", id: " + str(self.id)
