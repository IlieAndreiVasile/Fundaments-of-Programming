class Discipline:

    def __init__(self, disciplineID, name):
        self.__disciplineID = disciplineID
        self.__name = name

    def getDisciplineID(self):
        return self.__disciplineID

    def getName(self):
        return self.__name

    def setDisciplineID(self, disciplineID):
        self.__disciplineID = disciplineID

    def setName(self, name):
        self.__name = name

    def __str__(self):
        return "discipline id: " + str(self.__disciplineID) + "\tdiscipline name: " + str(self.__name)
