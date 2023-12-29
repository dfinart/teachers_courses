class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print("Course not found for this teacher")

    def edit_teacher(self, name, age):
        self.name = name
        self.age = age

    def show_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours


teachers = []
courses = []


def add_teacher(name, age):
    teacher = Teacher(name, age)
    teachers.append(teacher)
    return teacher


def add_course(name, hours):
    course = Course(name, hours)
    courses.append(course)
    return course


def remove_teacher(teacher):
    if teacher in teachers:
        teachers.remove(teacher)
    else:
        print("Teacher not found")


def remove_course(course):
    if course in courses:
        courses.remove(course)
    else:
        print("Course not found")


# Пример использования:

# Создание преподавателей и курсов
teacher1 = add_teacher("Иванов Иван Иванович", 35)
teacher2 = add_teacher("Петров Петр Петрович", 40)

course1 = add_course("Математика", 60)
course2 = add_course("Физика", 80)

# Добавление курсов преподавателям
teacher1.add_course(course1)
teacher1.add_course(course2)
teacher2.add_course(course1)

# Удаление курса у преподавателя
teacher1.remove_course(course2)

# Вывод курсов преподавателя
print(teacher1.show_courses())
print(teacher2.show_courses())

# Удаление преподавателя
remove_teacher(teacher2)

# Вывод всех преподавателей и курсов
for teacher in teachers:
    print("Teacher:", teacher.name)
    print("Courses:", teacher.show_courses())

for course in courses:
    print("Course:", course.name)
    print("Hours:", course.hours)
