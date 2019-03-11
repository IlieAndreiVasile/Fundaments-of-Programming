from domain import Student

class StudentRepository:

    def __init__(self):
        self.__data = []

    def findID(self, id):
        for i in self.__data:
            if i.getStudentID() == id:
                return i

    def add(self, student):
        if self.findID(student.getStudentID()) is not None:
            raise StudentRepositoryException("Student already exists!")
        self.__data.append(student)

    def remove(self, student):
        if self.findID(student) is None:
            raise StudentRepositoryException("Student does not exist!")
        for i in self.__data:
            if i.getStudentID() == student:
                self.__data.remove(i)

    def update(self, student):
        s = self.findID(student.getStudentID())
        if s is None:
            raise StudentRepositoryException("Student does not exist!")
        i = self.__data.index(s)
        self.__data.remove(s)
        self.__data.insert(i, student)

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
        String representation of student repository
        """
        s = ""
        for e in self.__data:
            s += str(e) + " "


class StudentRepositoryException(Exception):
    """
    Exception class for repository errors
    """
    def __init__(self, message):
        """
        Constructor for student repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
