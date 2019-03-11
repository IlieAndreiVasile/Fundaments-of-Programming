class Grade:

    def __init__(self, disciplineID, studentID, grade_value):
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__grade_value = grade_value

    def getDisciplineID(self):
        return self.__disciplineID

    def getStudentID(self):
        return self.__studentID

    def getGradeValue(self):
        return self.__grade_value

    def setDisciplineID(self, disciplineID):
        self.__disciplineID = disciplineID

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setGradeValue(self, grade_value):
        self.__grade_value = grade_value

    def __str__(self):
        return "discipline ID: " + str(self.__disciplineID) + "\tstudent ID: " + str(self.__studentID) \
               + "\tgrade value: " + str(self.__grade_value)
