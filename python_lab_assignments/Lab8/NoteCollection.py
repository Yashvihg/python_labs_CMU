# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani


class NoteCollection:

    def __init__(self):
        self._noteList = []

    def add(self, note):
        self._noteList.append(note)

    def getAllNotes(self):
        return self._noteList

    def getNoteByNumber(self, number):
        for note in self._noteList:
            if note.getNoteNumber() == number:
                return note
        return None

    def getNoteByName(self, name):
        matches = []
        for note in self._noteList:
            if note.getName() == name:
                matches.append(note)
        return matches
