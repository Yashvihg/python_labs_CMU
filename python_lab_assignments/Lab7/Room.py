# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from SensorCollection import SensorCollection
from AlarmCollection import AlarmCollection


class Room:
    """Represents a rectangular room that contains sensors, alarms, and a device."""

    def __init__(self, length=0.0, width=0.0, name="Unnamed", id=0):
        """Creates a Room with default or given length, width, name, and id."""
        self.length = length
        self.width = width
        self.name = name
        self.id = id
        self.sensors = SensorCollection()
        self.alarms = AlarmCollection()
        self.device = None

    def addSensor(self, sensor):
        """Adds a Sensor object to the room's SensorCollection."""
        self.sensors.add(sensor)

    def addAlarm(self, alarm):
        """Adds an Alarm object to the room's AlarmCollection."""
        self.alarms.add(alarm)

    def addDevice(self, device):
        """Assigns the Device object to the room."""
        self.device = device

    def display(self):
        """Prints the room, its device (if any), and its sensors and alarms."""
        print(self)
        if self.device is not None:
            print(self.device)
        self.sensors.display()
        self.alarms.display()

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
