from controller.DisciplineController import DisciplineController
from controller.GradeController import GradeController
from controller.StudentController import StudentController
from domain.Discipline import Discipline
from domain.Grade import Grade
from domain.Student import Student
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from repository.StudentRepository import StudentRepository


class UI:

    def printMenu(self):
        s = "\n \t \t MENU \n"
        s += "\n \t 1. Print students."
        s += "\n \t 2. Add student."
        s += "\n \t 3. Remove student."
        s += "\n \t 4. Update student."
        s += "\n \t 5. Print disciplines."
        s += "\n \t 6. Add discipline"
        s += "\n \t 7. Remove discipline."
        s += "\n \t 8. Update discipline."
        s += "\n \t 9. Add grade."
        s += "\n \t 10. Print grades."
        s += "\n \t 0. Exit."
        print(s)

    def mainMenu(self):
        studentRepo = StudentRepository()
        disciplineRepo = DisciplineRepository()
        gradeRepo = GradeRepository()

        studentRepo.add(Student(1, "Andrei"))
        studentRepo.add(Student(2, "Diana"))
        studentRepo.add(Student(3, "Tudor"))
        studentRepo.add(Student(4, "Alex"))
        studentRepo.add(Student(5, "Daniel"))
        studentRepo.add(Student(6, "Alin"))
        studentRepo.add(Student(7, "Sergiu"))
        studentRepo.add(Student(8, "Mihai"))
        studentRepo.add(Student(9, "Monica"))
        studentRepo.add(Student(10, "Denisa"))

        disciplineRepo.add(Discipline(1, "Fundaments of Programming"))
        disciplineRepo.add(Discipline(2, "Object oriented Programming"))
        disciplineRepo.add(Discipline(3, "Advanced Methods of Programming"))
        disciplineRepo.add(Discipline(4, "Computer Networks"))
        disciplineRepo.add(Discipline(5, "Computer's Architecture"))
        disciplineRepo.add(Discipline(6, "Operating Systems"))
        disciplineRepo.add(Discipline(7, "Database Management"))
        disciplineRepo.add(Discipline(8, "Mobile Applications"))
        disciplineRepo.add(Discipline(9, "Web Programming"))
        disciplineRepo.add(Discipline(10, "Artificial Intelligence"))

        gradeRepo.add(Grade(1, 1, 10))
        gradeRepo.add(Grade(1, 1, 7))
        gradeRepo.add(Grade(1, 1, 8))
        gradeRepo.add(Grade(1, 2, 9))
        gradeRepo.add(Grade(1, 3, 9))
        gradeRepo.add(Grade(1, 4, 9))
        gradeRepo.add(Grade(1, 5, 9))
        gradeRepo.add(Grade(2, 5, 10))
        gradeRepo.add(Grade(2, 6, 10))
        gradeRepo.add(Grade(2, 7, 10))
        gradeRepo.add(Grade(2, 8, 10))
        gradeRepo.add(Grade(2, 9, 10))
        gradeRepo.add(Grade(2, 10, 10))
        gradeRepo.add(Grade(3, 7, 6))
        gradeRepo.add(Grade(4, 3, 5))
        gradeRepo.add(Grade(5, 4, 7))

        studentCtrl = StudentController(studentRepo)
        disciplineCtrl = DisciplineController(disciplineRepo)
        gradeCtrl = GradeController(gradeRepo)

        while True:
            self.printMenu()
            cmd = int(input("Enter command: "))
            if cmd == 0:
                break
            elif cmd == 1:
                for s in studentCtrl.getAll():
                    print(str(s))
            elif cmd == 2:
                s = UI.readStudent()
                studentCtrl.add(s)
            elif cmd == 3:
                s = UI.readStudentID()
                studentCtrl.remove(s.getStudentID())
                gradeCtrl.removeByStudent(s.getStudentID())
            elif cmd == 4:
                s = UI.readStudent()
                studentCtrl.update(s)
            elif cmd == 5:
                for d in disciplineCtrl.getAll():
                    print(str(d))
            elif cmd == 6:
                d = UI.readDiscipline()
                disciplineCtrl.add(d)
            elif cmd == 7:
                d = UI.readDisciplineID()
                disciplineCtrl.remove(d.getDisciplineID())
                gradeCtrl.removeByDiscipline(d.getDisciplineID())
            elif cmd == 8:
                d = UI.readDiscipline()
                disciplineCtrl.update(d)
            elif cmd == 9:
                g = UI.readGrade()
                gradeCtrl.add(g)
            elif cmd == 10:
                for g in gradeCtrl.getAll():
                    print(str(g))
            else:
                print("Invalid command!")

    @staticmethod
    def readStudent():
        """
        Reads a student
        """
        try:
            id = int(input("\n \t Student ID: "))
            name = input("\n \t Student name: ")
            return Student(id, name)
        except ValueError:
            return Student(0, '')

    @staticmethod
    def readStudentID():
        """
        Reads a student
        """
        try:
            id = int(input("\n \t Student ID: "))
            return Student(id, '')
        except ValueError:
            return Student(0, '')

    @staticmethod
    def readDiscipline():
        """
        Reads a discipline
        """
        try:
            id = int(input("\n \t Discipline ID: "))
            name = input("\n \t Discipline name: ")
            return Discipline(id, name)
        except ValueError:
            return Discipline(0, '')

    @staticmethod
    def readDisciplineID():
        """
        Reads a discipline
        """
        try:
            id = int(input("\n \t Discipline ID: "))
            return Discipline(id, '')
        except ValueError:
            return Discipline(0, '')

    @staticmethod
    def readGrade():
        """
        Reads a grade of a discipline and student
        """
        try:
            dID = int(input("\n \t Discipline ID: "))
            sID = int(input("\n \t Student ID: "))
            grade = int(input("\n \t Grade: "))
            return Grade(dID, sID, grade)
        except ValueError:
            return Grade(0, 0, 0)
