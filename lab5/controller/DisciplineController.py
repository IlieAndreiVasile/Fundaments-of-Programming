class DisciplineController:

    def __init__(self, repo):
        self.__repo = repo

    def add(self, discipline):
        self.__repo.add(discipline)

    def remove(self, discipline):
        self.__repo.remove(discipline)

    def update(self, discipline):
        self.__repo.update(discipline)

    def getAll(self):
        """
        Write specification here
        """
        return self.__repo.getAll()


class DisciplineControllerException(Exception):
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
