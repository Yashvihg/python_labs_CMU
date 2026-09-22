# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class SensorCollection:
    """Represents a collection of Sensor objects."""

    def __init__(self):
        """Creates a SensorCollection with an empty list of sensors."""
        self.sensors = []

    def add(self, sensor):
        """Adds a Sensor object to the collection."""
        self.sensors.append(sensor)

    def display(self):
        """Displays each Sensor object in the collection."""
        for sensor in self.sensors:
            print(sensor)
