# Reading Files!!!
# 2020/08/10
# Today I am a man !!!
# I hope...

def remove_double_backslash(self, s_data):
    try:
        i_bs_found = s_data.index("\\")
    except
        return s_data

    b_db_found = True
    while b_db_found:
        s_left = s_data[0:i_bs_found - 1]
        s_right = s_data[i_bs_found +1:]
        s_data = s_left + s_right
        try:
            i_bs_found = s_data.index("\\", i_bs_found + 1)
        except
            return s_data



# Open External File
print("*** Open file")
employee_file = open("employees.txt", "r")  # Read only (w) Write (a) Append (r+) Read & Write

# Check if file is readable
print("*** Check if file is readable ***")
if employee_file.readable():
    print("Readable")
else:
    print("Not Readable")

# Read all lines into a list
print("\n*** Read all lines into an list")
emps = employee_file.readlines()

print(f"\nEmployee Read List\n{str(emps)}")

emps2 = []
print("\n- - - Employees - - -")

for emp in emps:
    print(emp)

print("\n- - - Remove Carriage Return - - -")

for emp in emps:
    ln: int = len(emp) - 1
    empx = emp[0:ln]
    print(empx)
    emps2.append(empx)

print("\nEmployee Altered List\n" + str(emps2))

# Close File
print("***Close file")
employee_file.close()
