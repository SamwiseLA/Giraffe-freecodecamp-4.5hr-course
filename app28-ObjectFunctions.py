from Student import Student

# Class Functions aka Methods: a function that is in the class that belongs to any instantiated Object

students = []

students.append(Student("Aaron", "Samwise", "Music", 4.0, False))
students.append(Student("Sandoval", "Heidi", "Music", 3.9, False))
students.append(Student("Dummy", "Bob", "Lunch", 1.3, True))


for student in students:
    if student.f_on_honor_roll():
        x = "Honor Roll"
    else:
        x = ""
    print(f"Name: {student.s_namel}, {student.s_namef} {x}")
