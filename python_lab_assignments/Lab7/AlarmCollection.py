# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class AlarmCollection:
    """Represents a collection of Alarm objects."""

    def __init__(self):
        """Creates an AlarmCollection with an empty list of alarms."""
        self.alarms = []

    def add(self, alarm):
        """Adds an Alarm object to the collection."""
        self.alarms.append(alarm)

    def display(self):
        """Displays each Alarm object in the collection."""
        for alarm in self.alarms:
            print(alarm)
