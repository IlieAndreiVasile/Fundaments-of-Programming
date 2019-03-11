class GradeController:

    def __init__(self, repo):
        self.__repo = repo

    def add(self, grade):
        self.__repo.add(grade)

    def removeByStudent(self, id):
        self.__repo.removeByStudent(id)

    def removeByDiscipline(self, id):
        self.__repo.removeByDiscipline(id)

    def getAll(self):
        """
        Write specification here
        """
        return self.__repo.getAll()
