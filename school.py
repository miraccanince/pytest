class TooManyStudents(Exception):
    pass


class Classrom:

    def __init__(self, teacher, students, course_title) -> None:
        self.teacher  = teacher
        self.students = students
        self.course_title = course_title

    
    def add_student(self,student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudents
    
    def remove_student(self,name):
        for student in self.students:
            if self.students == name:
                self.students.remove(student)
                break
    
    def change_teacher(self,new_teacher):
        self.teacher = new_teacher

class Person:
    def __init__(self, name):
        self.name = name
    
class Teacher(Person):
    pass

class Student(Person):
    pass