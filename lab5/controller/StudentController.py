from repository import StudentRepository

class StudentController:

    def __init__(self, repo):
        self.__repo = repo

    def add(self, student):
        self.__repo.add(student)

    def remove(self, student):
        self.__repo.remove(student)

    def update(self, student):
        self.__repo.update(student)

    def getAll(self):
        """
        Write specification here
        """
        return self.__repo.getAll()


class StudentControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for student controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
