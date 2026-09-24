# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from Note import Note


class Memo(Note):

    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body)
        self._fromPerson = fromPerson
        self._toPerson = toPerson

    def getFromPerson(self):
        return self._fromPerson

    def getToPerson(self):
        return self._toPerson

    def __str__(self):
        return (f"From: {self._fromPerson}\n"
                f"To: {self._toPerson}\n"
                f"{super().__str__()}")
