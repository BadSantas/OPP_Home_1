class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course].append(grade)
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.lectures_grades.values())
        total_count = sum(len(grades) for grades in self.lectures_grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grade_students(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count != 0 else 0

def average_grade_lecturers(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.lectures_grades:
            total_grades += sum(lecturer.lectures_grades[course])
            total_count += len(lecturer.lectures_grades[course])
    return total_grades / total_count if total_count != 0 else 0

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('Введение в программирование')

student2 = Student('Jane', 'Doe', 'female')
student2.courses_in_progress.append('Python')
student2.finished_courses.append('Введение в программирование')

lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer('Alice', 'Smith')
lecturer2.courses_attached.append('Python')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached.append('Python')

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached.append('Python')

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 8)

print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

print(lecturer1 > lecturer2)

students = [student1, student2]
average_student_grade = average_grade_students(students, 'Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {average_student_grade:.1f}")

lecturers = [lecturer1, lecturer2]
average_lecturer_grade = average_grade_lecturers(lecturers, 'Python')
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade:.1f}")