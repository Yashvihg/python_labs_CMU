# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from Sensor import Sensor
from Device import Device
from Room import Room
from Alarm import Alarm


class Lab6:
    """Driver class that demonstrates each class and runs the kitchen monitoring program."""

    @staticmethod
    def main():
        """Demonstrates Sensor, Device, Room, and Alarm (checkpoint), then runs the Lab 6 driver program."""
        # solution 2
        print("--- Sensor ---")
        sensor = Sensor(minimum=0.0, maximum=120.0, currentValue=68.0, interval=1, location="Kitchen",
                         type="Temperature", id=1)
        print(sensor)
        print("Tripped:", sensor.trip())

        sensor.setCurrentValue(120)
        print(sensor)
        print("Tripped:", sensor.trip())

        # solution 3
        print("\n--- Device ---")
        device = Device(type="Camera", location="Front Door", id=2)
        print(device)
        device.actuate()

        # solution 4
        print("\n--- Room ---")
        room = Room(length=12.5, width=10.0, name="Living Room", id=3)
        print(room)
        print("Area:", room.getArea())

        # solution 5
        print("\n--- Alarm ---")
        alarm = Alarm(message="Fire detected!", id=4)
        print(alarm)
        alarm.soundTheAlarm()

        # solution 6
        print("\nLab 6 Driver")
        temperature = Sensor(0.0, 120.0, 68.0, 1.0, "kitchen", "temperature", 1)
        extinguisher = Device("fire extinguisher", "kitchen", 1)
        kitchen = Room(12.0, 15.0, "kitchen", 1)
        bell = Alarm("Ding! Ding!", 1)

        print(temperature)
        print(extinguisher)
        print(kitchen)
        print(bell)

        # solution 7
        print("\nWelcome to the Smart Kitchen Monitoring System!")
        print(kitchen)

        original_temperature = temperature.getCurrentValue()

        choice = input("\nWould you like to enter a new temperature value? (Y/N): ").strip().upper()
        while choice == "Y":
            print("Current kitchen temperature:", temperature.getCurrentValue())
            new_value = float(input("Enter a new temperature: "))
            temperature.setCurrentValue(new_value)

            if temperature.trip():
                print("\nWarning! The kitchen temperature is out of the safe range!")
                extinguisher.actuate()
                bell.soundTheAlarm()
            else:
                print("Temperature is within the safe range.")

            temperature.setCurrentValue(original_temperature)
            choice = input("\nWould you like to enter a new temperature value? (Y/N): ").strip().upper()

        # solution 8
        print("\n--- Reflection Questions ---")
        print("a. Sensor and Room are responsible for storing data (e.g., Sensor holds minimum, maximum, and "
              "currentValue; Room holds length, width, and name). Device and Alarm are responsible for performing "
              "actions (e.g., Device.actuate() and Alarm.soundTheAlarm()).")
        print("b. Placing behavior inside classes keeps related data and logic bundled together, so each class "
              "manages its own responsibilities. This makes the code easier to read, reuse, and maintain than "
              "putting all the logic directly in main().")
        print("c. During the monitoring loop, the Sensor, Device, and Alarm objects work together through main(): "
              "the Sensor's trip() method checks whether the new currentValue is outside the safe range; if it is, "
              "main() calls the Device's actuate() method to activate the fire extinguisher and the Alarm's "
              "soundTheAlarm() method to alert someone, with main() coordinating the interaction between the "
              "three objects.")


if __name__ == "__main__":
    Lab6.main()
