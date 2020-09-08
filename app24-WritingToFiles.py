# Writing To Files!!!
# 2020/08/11
# Today I am a man more of a man!!!
# She hopes...

# Open External File
print("*** Open file ***")

b_opened_file = True

try:
    employee_file = open("employees.txt", "r")  # Read only (w) Write (a) Append (r+) Read & Write
except :
    b_opened_file = False
    print("File Open Error")

if not b_opened_file:
    exit()

b_readable = True
# Check if file is readable
print("*** Check if file is readable ***")

if employee_file.readable():
    print("*** Readable ***\n--------------------")
else:
    print("*** Not Readable ***")
    b_readable = False

if b_readable:
    print(employee_file.read())

employee_file.close()

print("-----------> Append Section <------------")

# Open External File
print("*** Open file ***")

b_opened_file = True

try:
    employee_file = open("employees.txt", "a")  # (r) Read only (w) Write (a) Append (r+) Read & Write
except :
    b_opened_file = False
    print("File Open Error")

if not b_opened_file:
    exit()

print("Enter Blank to Bypass")
s_append = "\n" + input("Name: ") + " - " + input("Department: ")

if s_append[1] != " ":

    employee_file.write(s_append)
    print("*** Appended Files ***")

    employee_file.close()

print("-----------> Write Section <------------")

# Open External File
print("*** Open file ***")

b_opened_file = True

s_emp_file_name = input("Enter New Employee File Name: ") + ".txt"
try:
    employee_file = open(s_emp_file_name, "w")  # (r) Read only (w) Write (a) Append (r+) Read & Write
except :
    b_opened_file = False
    print("File Open Error")

if not b_opened_file:
    exit()

s_write = "??"
s_write_list = ""
s_pre = ""

while s_write[1] != " ":
    if s_write != "??":
        s_pre = "\n"
    print("*** Please Enter Next Employee Info - BLANK to End Input ***")
    s_write = s_pre + input("Name: ") + " - " + input("Department: ")
    if s_write[1] != " ":
            s_write_list = s_write_list + s_write
    elif s_write[0] != "-" and s_write[0] != "\n" :
        s_write_list = s_write_list + s_write
        s_write = "--"

employee_file.write(s_write_list)
print("*** Wrote File ***")

employee_file.close()
