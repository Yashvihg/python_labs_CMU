# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

class Alarm:
    """Represents an alarm that displays a message and simulates an emergency call."""

    def __init__(self, message="Intruder detected!", id=0):
        """Creates an Alarm with default or given message and id."""
        self.message = message
        self.id = id

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def soundTheAlarm(self):
        """Displays the alarm message and simulates calling 911."""
        print(self.message)
        print("Dialing 911...")
        print("Connected to emergency services. Reporting alarm id " + str(self.id) + ".")

    def __str__(self):
        return "message: " + str(self.message) + ", id: " + str(self.id)
