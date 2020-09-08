# Class is a Programmer Defined datatype - or a complex combination of
# regular datatypes to represent a more complex data
# Like, a person would have a name, birthday, address, shoe size, eye color.
#
# The class is defined in it's own file -
# The Object utilizes the class structure to create actual data
#
#
# the 1st "Student" is the class file,
# the 2nd "Student" is the class in the Student.py file,
# it's structure is used to create Objects
#

from Student import Student

# Function to get Info for Each Student


def f_input_students():
    s_namel_input = input("Enter Last Name: ")
    s_namef_input = ""
    s_major_input = ""
    f_gpa_input = 0
    b_is_on_probation_input = False
    if s_namel_input != "":
        s_namef_input = input("Enter First Name: ")
        s_major_input = input("Enter Major: ")
        f_gpa_input = float(input("Enter gpa: "))
        s_is_on_probation_input = input("Enter is on Probation(T/F): ")
        if s_is_on_probation_input[0].upper() == "T":
            b_is_on_probation_input = True
        else:
            b_is_on_probation_input = False

    return [s_namel_input, s_namef_input, s_major_input, f_gpa_input, b_is_on_probation_input]

# ------------------- Module Starts Here --------------------------


l_students = ([])


b_start = True
s_namel_input_empty = "?"
while b_start or s_namel_input_empty != "":
    b_start = False
    student_data = f_input_students()
    # print(student_data)
    s_namel_input_empty = student_data[0]
    if student_data[0] != "":
        l_students.append(Student(student_data[0], student_data[1],
                                  student_data[2], student_data[3], student_data[4], ))


# print(l_students[0])
print("-----------------------")
i_cnt = 0
for studentx in l_students:
    i_cnt += 1
    if studentx.b_is_on_probation:
        s_prob = "*"
    else:
        s_prob = " "
    print("{5}Student{5} {4}: {1} {0} Majors in {2}, with  GPA of {3}".format(studentx.s_namel,
                                                                              studentx.s_namef, studentx.s_major,
                                                                              studentx.f_gpa, i_cnt, s_prob))

print("-------- End ----------")
