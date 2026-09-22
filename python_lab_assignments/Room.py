# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class Room:
    """Represents a rectangular room identified by length, width, name, and id."""

    def __init__(self, length=0.0, width=0.0, name="Unnamed", id=0):
        """Creates a Room with default or given length, width, name, and id."""
        self.length = length
        self.width = width
        self.name = name
        self.id = id

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getArea(self):
        """Computes and returns the room's area."""
        return self.length * self.width

    def __str__(self):
        return ("length: " + str(self.length) +
                ", width: " + str(self.width) +
                ", name: " + str(self.name) +
                ", id: " + str(self.id))
