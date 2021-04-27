class Student:

    default = "student"

    def __init__(self):
        self.name = Student.default
        self.age = Student.default
        self.class_ = Student.default

    def set_info(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def grade_calc(self, h, a, f):
        self.percent = (h + a + f)*100/175
        bound = {80: 'A', 70: 'B', 60: 'C', 50: 'D'}
        for x in bound:
            if self.percent > x:
                self.grade = bound[x]
                return f"You scored {self.percent}%. Your grade is {self.grade}"
                break
            else:
                continue
        else:
            return f"You scored {self.percent}%. Sorry, you did not pass"


john = Student()
print(john.name)
john.set_info('John', 23, 'Bio')
print(john.name)
print(john.grade_calc(20, 40, 78))
