import unittest
from repository.repository import *


class Test(unittest.TestCase):

    def test_domain(self):
        s = Student(1, "Andrei")
        assert s.getID() == 1
        assert s.getName() == "Andrei"
        s.setID(3)
        s.setName("Alin")
        assert s.getID() == 3
        assert s.getName() == "Alin"

        d = Discipline(4, "fp")
        assert d.getID() == 4
        assert d.getName() == "fp"
        d.setID(7)
        d.setName("asc")
        assert d.getID() == 7
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
        sr = studentRepository()
        dr = disciplineRepository()
        gr = gradeRepository()

        assert len(sr) == 0
        sr.add(Student(9, "Tudor"))
        assert len(sr) == 1
        s = Student(2, 'Andrei')
        assert sr.find(s.getID()) == 0
        s = Student(9, 'Diana')
        sr.update(s)
        assert sr.findIDWithName('Diana') == 9
        sr.remove(9)
        assert len(sr) == 0

        assert len(dr) == 0
        dr.add(Discipline(2, "fp"))
        assert len(dr) == 1
        d = Discipline(4, 'asc')
        assert dr.find(d.getID()) == 0
        d = Discipline(2, 'lftc')
        dr.update(d)
        assert dr.findIDWithName('lftc') == 2
        dr.remove(2)
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
