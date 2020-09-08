# Reading Files!!!
# 2020/08/10
# Today I am a man !!!
# I hope...

def remove_double_backslash(s_data):
    # print("")
    try:
        i_bs_found = s_data.index("\\n")
    except ValueError:
        return s_data

    b_db_found = True
    while b_db_found:
        s_left = s_data[0:i_bs_found]
        s_right = s_data[i_bs_found + 2:]
        s_data = s_left + '\n' + s_right
        try:
            i_bs_found = s_data.index("\\n", i_bs_found + 1)
        except ValueError:
            return s_data


def get_questions():

    # Open External File
    print("*** Open file ***")
    questions_file = open("app27_Questions.txt", "r")  # Read only (w) Write (a) Append (r+) Read & Write

    # Check if file is readable
    # print("*** Check if file is readable ***")
    if questions_file.readable():
        print("Readable")
    else:
        print("Not Readable")

    # Read all lines into a list
    # print("\n*** Read all lines into an list")
    questions = questions_file.readlines()

    # print(f"\nQuestions Read List\n{str(questions)}")

    # questions2 = []
    # print("\n- - - Questions - - -")

    # for ques in questions:
    #    print(ques)

    # print("\n- - - Remove Carriage Return - - -")

    # Close File
    print("***Close file")
    questions_file.close()

    l_parsed_data = []
    for row in questions:
        l_parsed_data.append(remove_double_backslash(row))

    # print("")

    return l_parsed_data
