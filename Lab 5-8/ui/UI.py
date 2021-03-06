from controller.Statistics import *
from repository.studentsFileRepository import *
from repository.disciplinesFileRepository import *
from repository.gradesFileRepository import *
from repository.studentsPickleFileRepository import *
from repository.disciplinesPickleFileRepository import *
from repository.gradesPickleFileRepository import *


class UI:

    def printMenu(self):
        
        string = "\n \t         MENU \n"
        string += "\n \t 1. Add student."
        string += "\n \t 2. Add discipline"
        string += "\n \t 3. Remove student."
        string += "\n \t 4. Remove discipline."
        string += "\n \t 5. Update student."
        string += "\n \t 6. Update discipline."
        string += "\n \t 7. Add grade."
        string += "\n \t 8. Search student by ID."
        string += "\n \t 9. Search student by name."
        string += "\n \t 10. Search discipline by ID."
        string += "\n \t 11. Search discipline by name."
        string += "\n \t 12. Sort students enrolled at a discipline alphabetically."
        string += "\n \t 13. Sort students by descending order of average grade."
        string += "\n \t 14. Students failing at a discipline."
        string += "\n \t 15. Students with the best school situation."
        string += "\n \t 16. Disciplines with at least one grade."
        string += "\n \t 17. Redo."
        string += "\n \t 18. Undo."
        string += "\n \t 19. Print students."
        string += "\n \t 20. Print disciplines."
        string += "\n \t 21. Print grades."
        string += "\n \t 0. Exit."
        print(string)


    def mainMenu(self):

        studentRepo = studentRepository()
        disciplineRepo = disciplineRepository()
        gradeRepo = gradeRepository()

        undoController = undo()
        undoController.newOperation()

        U = UI()

        command = U.readFromSettingsFile()

        sem = True

        if command == 'binaryfiles':
            studentFile = studentsPickleFileRepository(studentRepo)
            studentFile.readFromStudentsFile()

            disciplineFile = disciplinesPickleFileRepository(disciplineRepo)
            disciplineFile.readFromDisciplinesFile()

            gradeFile = gradesPickleFileRepository(gradeRepo)
            gradeFile.readFromGradesFile()

        elif command == 'inmemory':
            studentFile = studentsFileRepository(studentRepo)
            studentFile.readFromStudentsFile()

            disciplineFile = disciplinesFileRepository(disciplineRepo)
            disciplineFile.readFromDisciplinesFile()

            gradeFile = gradesFileRepository(gradeRepo)
            gradeFile.readFromGradesFile()

        else:
            print('\n \t Invalid settings !')
            print('\n \t Change the settings in valid ones!')
            sem = False


        student = studentController(studentRepo, undoController, gradeRepo)
        discipline = disciplineController(disciplineRepo, undoController, gradeRepo)
        grade = gradeRepositoryController(gradeRepo, studentRepo, disciplineRepo, undoController)

        command = -1

        while command != 0 and sem is True:

            x = statisticController(student, discipline, grade)
            statistics = Statistics(x)

            U.printMenu()
            
            command = input("\n Your command: ")

            if command == '0':
                print('\n \t Bye!')
                break

            elif command == '1':
                x = U.readStudent()
                try:
                    if student.find(x.getID()) == 0:
                        undoController.newOperation()
                        student.add(x)
                        studentFile.writeToStudentsFile()
                        print("\n \t The student has been added !")
                    else: print("\n Student already exists !")
                except:
                    pass

            elif command == '2':
                x = U.readDiscipline()
                try:
                    if discipline.find(x.getID()) == 0:
                        undoController.newOperation()
                        discipline.add(x)
                        disciplineFile.writeToDisciplinesFile()
                        print("\n \t The discipline has been added !")
                    else: print("\n Discipline already exists !")
                except:
                    pass

            elif command == '3':           
                x = U.readStudentID()
                if student.find(x.getID()) != 0:
                    undoController.newOperation()
                    student.remove(x.getID())
                    grade.removeByStudent(x.getID())
                    studentFile.deleteFromStudentsFile(x.getID())
                    gradeFile.deleteFromGradesFile(x.getID())
                    print("\n \t The student has been removed !")
                else:
                    print("\n The student does not exist !")

            elif command == '4':
                x = U.readDisciplineID()
                if discipline.find(x.getID()) != 0:
                    undoController.newOperation()
                    discipline.remove(x.getID())
                    grade.removeByDiscipline(x.getID())
                    disciplineFile.deleteFromDisciplinesFile(x.getID())
                    gradeFile.deleteFromGradesFile(x.getID())
                    print("\n \t The discipline has been removed !")
                else:
                    print("\n The discipline does not exist !")

            elif command == '5':
                x = U.readStudent()
                if student.find(x.getID()) != 0:
                    undoController.newOperation()
                    student.update(x)
                    studentFile.writeToStudentsFile()
                    print("\n \t Updated !")
                else:
                    print("\n The student does not exist !")
                
            elif command == '6':
                x = U.readDiscipline()
                if discipline.find(x.getID()) != 0:
                    undoController.newOperation()
                    discipline.update(x)
                    disciplineFile.writeToDisciplinesFile()
                    print("\n \t Updated !")
                else:
                    print("\n The discipline does not exist !")
                
            elif command == '7':
                x = U.readGrade()
                if x.getGradeValue() >= 1 and x.getGradeValue() <= 10:
                    if student.find(x.getStudentID()) != 0 and discipline.find(x.getDisciplineID()) != 0:
                        undoController.newOperation()
                        grade.add(x)
                        gradeFile.writeToGradesFile()
                        print("\n \t Grade has been added !")
                    else: print("\n Invalid data !")
                else:
                    print("\n Invalid data !")

            elif command == '8':
                x = U.readStudentID()
                if x.getID() != 0:
                    if student.find(x.getID()) != 0:
                        print('\n')
                        print(student.listByID(x.getID()))
                    else: print("\n Invalid data !")
                else:
                    print("\n Invalid data !")

            elif command == '9':
                x = U.readStudentName()
                if student.findName(x.getName()) != 0:
                    print('\n')
                    print(student.listByName(x.getName()))
                else:
                    print("\n Invalid data !")

            elif command == '10':
                x = U.readDisciplineID()
                if x.getID() != 0:
                    if discipline.find(x.getID()) != 0:
                        print('\n')
                        print(discipline.listByID(x.getID()))
                    else: print("\n Invalid data !")
                else:
                    print("\n Invalid data !")

            elif command == '11':
                x = U.readDisciplineName()
                if discipline.findName(x.getName()) != 0:
                    print('\n')
                    print(discipline.listByName(x.getName()))
                else: print("\n Invalid data !")


            elif command == '12': print(statistics.sortAlphabetically())

            elif command == '13': print(statistics.sortAverageGrade())

            elif command == '14': print(statistics.failing())

            elif command == '15': print(statistics.bestSchoolSituation())

            elif command == '16': print(statistics.oneGrade())

            elif command == '17':
                if undoController._index <= len(undoController._operations) - 2:
                    undoController.redo()
                    studentFile.writeToStudentsFile()
                    disciplineFile.writeToDisciplinesFile()
                    gradeFile.writeToGradesFile()
                    print("\n \t Redo done !")
                else:
                    print("\n \t You can't redo !")

            elif command == '18':
                if undoController._index != 0:
                    undoController.undo()
                    studentFile.writeToStudentsFile()
                    disciplineFile.writeToDisciplinesFile()
                    gradeFile.writeToGradesFile()
                    print("\n \t Undo done !")
                else:
                    print("\n \t You can't undo !")

            elif command == '19':
                print("\n \t         Student list: \n")
                print(str(student))
                print("\n \n")

            elif command == '20':
                print("\n \t        Discipline list \n")
                print(str(discipline))
                print("\n \n")

            elif command == '21':
                print("\n \t              Grade list \n")
                print(str(grade))
                print("\n \n")

            else:
                print("\n Invalid data !")


    def readStudent(self):
        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Student ID: "))
            name = input("\n \t Student name: ")
            return Student(ID, name)
        except ValueError: return Student(0, '')
        
    def readDiscipline(self):
        '''
        Reads a discipline
        '''

        try:
            ID = int(input("\n \t Discipline ID: "))
            name = input("\n \t Discipline name: ")
            return Discipline(ID, name)
        except ValueError: return Discipline(0, '')

    def readGrade(self):
        '''
        Reads a grade of a discipline and student
        '''

        try:
            dID = int(input("\n \t Discipline ID: "))
            sID = int(input("\n \t Student ID: "))
            grade = int(input("\n \t Grade: "))
            return Grade(dID, sID, grade)
        except ValueError:
            return Grade(0, 0, 0)

    def readStudentID(self):
        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Student ID: "))
            return Student(ID, '')
        except ValueError: return Student(0, '')

    def readStudentName(self):
        '''
        Reads a discipline
        '''

        name = input("\n \t Student name: ")
        return Student(0, name)

    def readDisciplineID(self):
        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Discipline ID: "))
            return Discipline(ID, '')
        except ValueError: return Discipline(0, '')

    def readDisciplineName(self):
        '''
        Reads a discipline
        '''

        name = input("\n \t Discipline name: ")
        return Discipline(0, name)

    def readFromSettingsFile(self):
        '''
        This function reads from Settings.txt file the current settings
        '''

        try:
            settingsFile = open("Settings.txt", "r")
            line = settingsFile.readline().strip()
            lx = line.split('=')
            settingsFile.close()
            return lx[1]
        except IOError:
            pass
