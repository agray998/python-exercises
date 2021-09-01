class Student:
    def __init__(self, name, age, class_ = "Student"):
        self.name = name
        self.age = age
        self.class_ = class_


    def grade_calc(self, h, a, f):
        self.percent = (h + a + f)*100/175
        bound = {80: 'A', 70: 'B', 60: 'C', 50: 'D'}
        for x in bound:
            if self.percent > x:
                self.grade = bound[x]
                return f"{self.name} scored {self.percent}%. {self.name}'s grade is {self.grade}"
                break
            else:
                continue
        else:
            return f"{self.name} scored {self.percent}%. Sorry, you did not pass"

john = Student('John', 23)
print(john.grade_calc(20, 40, 78))
