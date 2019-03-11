import unittest

from domain.Discipline import Discipline
from domain.Grade import Grade
from domain.Student import Student
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from repository.StudentRepository import StudentRepository


class Test(unittest.TestCase):

    def test_domain(self):
        s = Student(1, "Andrei")
        assert s.getStudentID() == 1
        assert s.getName() == "Andrei"
        s.setStudentID(3)
        s.setName("Alin")
        assert s.getStudentID() == 3
        assert s.getName() == "Alin"

        d = Discipline(4, "fp")
        assert d.getDisciplineID() == 4
        assert d.getName() == "fp"
        d.setDisciplineID(7)
        d.setName("asc")
        assert d.getDisciplineID() == 7
        assert d.getName() == "asc"

        g = Grade(2, 3, 5)
        assert g.getDisciplineID() == 2
        assert g.getStudentID() == 3
        assert g.getGradeValue() == 5
        g.setDisciplineID(7)
        g.setStudentID(6)
        g.setGradeValue(8)
        assert g.getDisciplineID() == 7
        assert g.getStudentID() == 6
        assert g.getGradeValue() == 8


    def test_repository(self):
        sr = StudentRepository()
        dr = DisciplineRepository()
        gr = GradeRepository()

        assert len(sr) == 0
        sr.add(Student(9, "Tudor"))
        assert len(sr) == 1
        sr.remove(9)
        assert len(sr) == 0

        assert len(dr) == 0
        dr.add(Discipline(3, "fp"))
        assert len(dr) == 1
        dr.remove(3)
        assert len(dr) == 0

        sr.add(Student(9, "Tudor"))
        dr.add(Discipline(3, "fp"))
        assert len(gr) == 0
        gr.add(Grade(3, 9, 7))
        assert len(gr) == 1
        gr.removeByStudent(9)
        assert len(gr) == 0
        # gr.removeByDiscipline(3)
        # assert len(gr) == 0



if __name__ == '__main__':
    unittest.main()
