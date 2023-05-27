class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def _calc_avg_grade(self):
        all_grades = []
        if len(self.grades):
            for item in self.grades.values():
                all_grades += item
            self._avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            self._avg_grade = []

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        self._calc_avg_grade()
        res += f"Средняя оценка за домашние задания: {self._avg_grade}\n"
        res += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        res += f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            self._calc_avg_grade()
            other._calc_avg_grade()
            return self._avg_grade < other._avg_grade
        else:
            return 'Можно сравнивать только студентов друг с другом'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def _calc_avg_grade(self):
        all_grades = []
        if len(self.grades_from_students):
            for item in self.grades_from_students.values():
                all_grades += item
            self._avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            self._avg_grade = []

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        self._calc_avg_grade()
        res += f"Средняя оценка за лекции: {self._avg_grade}\n"
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self._calc_avg_grade()
            other._calc_avg_grade()
            return self._avg_grade < other._avg_grade
        else:
            return 'Можно сравнивать только лекторов друг с другом'

def rate_list_of_students(students, course):
    grades_list = []
    for guy in students:
        if isinstance(guy, Student):
            if course in guy.grades:
                grades_list += guy.grades[course]
        else:
            print(f'{guy.name} {guy.surname} не студент')
    if len(grades_list):
        print(sum(grades_list)/len(grades_list))
    else:
        print('Ошибка')

def rate_list_of_lecturers(lecturers, course):
    grades_list = []
    for lect in lecturers:
        if isinstance(lect, Lecturer):
            if course in lect.grades_from_students:
                grades_list += lect.grades_from_students[course]
        else:
            print(f'{lect.name} {lect.surname} не лектор')
    if len(grades_list):
        print(sum(grades_list)/len(grades_list))
    else:
        print('Ошибка')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

great_lecturer = Lecturer('Cool', 'Guy')
great_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(great_lecturer, 'Python', 7)

print(best_student.grades)
print(great_lecturer.grades_from_students)

print(best_student)
print(great_lecturer)
print(cool_reviewer)

another_student = Student('Anna', 'Gubanova', 'female')
another_student.courses_in_progress += ['Python']
cool_reviewer.rate_hw(another_student, 'Python', 10)

print(best_student < another_student)

another_lecturer = Lecturer('Steve', 'Jobs')
another_lecturer.courses_attached += ['Python']
another_student.rate_lecturer(another_lecturer, 'Python', 9)

print(another_lecturer > great_lecturer)

rate_list_of_lecturers([another_lecturer, great_lecturer], 'Python')
rate_list_of_lecturers([another_student, great_lecturer, another_lecturer], 'Python')
rate_list_of_students([best_student, another_student], 'Python')
rate_list_of_students([best_student, another_student], 'C++')