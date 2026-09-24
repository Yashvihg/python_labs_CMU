# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from TimedMemo import TimedMemo


class PoliteTimedMemo(TimedMemo):

    DEFAULT_GREETING = "Dear"
    DEFAULT_CLOSING = "Yours truly,"

    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body, fromPerson, toPerson)

    def __str__(self):
        return (f"Date: {self._today}\n"
                f"Name: {self._name}\n"
                f"{PoliteTimedMemo.DEFAULT_GREETING} {self._toPerson}:\n"
                f"{self._body}\n"
                f"{PoliteTimedMemo.DEFAULT_CLOSING}\n"
                f"{self._fromPerson}\n"
                f"Note# {self._noteNumber}\n"
                f"{self._FOOTER}")
