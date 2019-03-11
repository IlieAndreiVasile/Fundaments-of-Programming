class Student:

    def __init__(self, studentID, name):
        self.__studentID = studentID
        self.__name = name

    def getStudentID(self):
        return self.__studentID

    def getName(self):
        return self.__name

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setName(self, name):
        self.__name = name

    def __str__(self):
        return "student id: " + str(self.__studentID) + "\tstudent name: " + str(self.__name)
