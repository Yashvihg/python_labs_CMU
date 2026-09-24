# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

from datetime import date


class FormattedDate:

    def __init__(self, dateValue=None):
        if dateValue is None:
            dateValue = date.today()
        self._dateValue = dateValue

    def getDate(self):
        return self._dateValue

    def __str__(self):
        return self._dateValue.strftime("%Y-%m-%d")
