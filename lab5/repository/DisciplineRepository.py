from domain import Discipline

class DisciplineRepository:

    def __init__(self):
        self.__data = []

    def findID(self, id):
        for i in self.__data:
            if i.getDisciplineID() == id:
                return i

    def add(self, discipline):
        if self.findID(discipline.getDisciplineID()) is not None:
            raise DiciplineRepositoryException("Discipline already exists!")
        self.__data.append(discipline)

    def remove(self, discipline):
        if self.findID(discipline) is None:
            raise DiciplineRepositoryException("Discipline does not exist!")
        for i in self.__data:
            if i.getDisciplineID() == discipline:
                self.__data.remove(i)

    def update(self, discipline):
        d = self.findID(discipline.getDisciplineID())
        if d is None:
            raise DiciplineRepositoryException("Discipline does not exist!")
        i = self.__data.index(d)
        self.__data.remove(d)
        self.__data.insert(i, discipline)

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        """
        String representation of discipline repository
        """
        s = ""
        for e in self.__data:
            s += str(e) + " "


class DiciplineRepositoryException(Exception):
    """
    Exception class for discipline repository errors
    """
    def __init__(self, message):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
