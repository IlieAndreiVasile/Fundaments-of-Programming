class GradeRepository:

    def __init__(self):
        self.__data = []

    def add(self, grade):
        """
        Adds a new item to the grade repository
        """
        self.__data.append(grade)

    def removeByStudent(self, id):
        """
        Removes an item by a student ID
        """
        for i in self.__data:
            if id == i.getStudentID():
                self.__data.remove(i)

    def removeByDiscipline(self, id):
        """
        Removes an item by a discipline ID
        """
        for i in self.__data:
            if id == i.getDisciplineID():
                self.__data.remove(i)

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
