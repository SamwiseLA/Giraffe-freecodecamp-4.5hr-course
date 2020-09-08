# Everything indented under the "class" will be the "Student" attributes
# You use and Initialize Function to set up a way to use the "class"
# def __init__(self, a, b, c, d...)
#
#
class Student:
    i_number_of_students = 0

    def __init__(self, s_nameli, s_namefi, s_majori, f_gpai, b_is_on_probationi) :
        self.s_namel = s_nameli
        self.s_namef = s_namefi
        self.s_major = s_majori
        self.f_gpa = f_gpai
        self.b_is_on_probation = b_is_on_probationi




    def f_on_honor_roll(self):
        if self.f_gpa > 3.5:
            return True
        else:
            return False
