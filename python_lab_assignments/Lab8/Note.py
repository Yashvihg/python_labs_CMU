# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

"""
Defines the Note class used in the Make A Note application.
A Note stores a name and body and serves as the parent class for all note types.
"""

class Note: 
    _noteCount = 0 
    _FOOTER = "***** Powered by Make-A-Note *****" 
    
    def __init__(self, name, body): 
        self._name = name 
        self._body = body 
        Note._noteCount += 1 # Increment how many notes have been created
        self._noteNumber = Note._noteCount # Set this note's id to the current count

    def getNoteNumber(self):
        return self._noteNumber

    def getName(self):
        return self._name

    def __str__(self): 
        return (f"Name: {self._name}\n" 
                f"Body: {self._body}\n" 
                f"Note# {self._noteNumber}\n" 
                f"{self._FOOTER}" )
    
