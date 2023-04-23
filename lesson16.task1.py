class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am a {self.gender}. I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, gender, grade_level, courses=None):
        super().__init__(name, age, gender)
        self.grade_level = grade_level
        self.courses = courses if courses else []

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        print(f"{self.name} is taking the following courses: {', '.join(self.courses)}.")


class Teacher(Person):
    def __init__(self, name, age, gender, salary, subject=None):
        super().__init__(name, age, gender)
        self.salary = salary
        self.subject = subject

    def give_raise(self, amount):
        self.salary += amount

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

person1 = Person("Alice", 25, "female")
person1.introduce()

student1 = Student("Bob", 16, "male", 10, ["Math", "Science"])
student1.add_course("English")
student1.list_courses()

teacher1 = Teacher("Charlie", 40, "male", 50000, "History")
teacher1.give_raise(10000)
teacher1.teach()
