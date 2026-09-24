# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from Memo import Memo
from FormattedDate import FormattedDate


class TimedMemo(Memo):

    def __init__(self, name, body, fromPerson, toPerson):
        super().__init__(name, body, fromPerson, toPerson)
        self._today = str(FormattedDate())

    def getToday(self):
        return self._today

    def __str__(self):
        return (f"Date: {self._today}\n"
                f"{super().__str__()}")
