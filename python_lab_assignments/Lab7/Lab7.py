# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from Sensor import Sensor
from Device import Device
from Room import Room
from Alarm import Alarm


def main():
    """Builds room1 with a device, 5 sensors, and 3 alarms, then swaps the device and displays the room."""
    # solution 4
    room1 = Room(12.0, 15.0, "kitchen", "#1")

    extinguisher = Device("fire extinguisher", "kitchen", "#1")
    room1.addDevice(extinguisher)

    for i in range(5):
        sensor = Sensor(0.0, 120.0, 68.0, 1.0, "kitchen", "temperature", i + 1)
        room1.addSensor(sensor)

    for i in range(3):
        alarm = Alarm("Ding! Ding!", i + 1)
        room1.addAlarm(alarm)

    print("--- room1 ---")
    room1.display()

    # solution 5
    chemicalFoamer = Device("chemical foamer", "kitchen", 2)
    room1.addDevice(chemicalFoamer)

    print("\n--- room1 after swapping the device ---")
    room1.display()
    # The temperature sensors are unaffected - addDevice() only replaces room1's single
    # Device reference. Sensors live in the separate SensorCollection, so they are still
    # there; display() still lists all 5 of them after the device is swapped.


if __name__ == "__main__":
    main()
