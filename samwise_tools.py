import random

def get_strleft_numright(s_input):
    i_len = len(s_input)
    #print(i_len)
    i_pos_check = i_len
    i_pos_check = i_pos_check - 1
    b_num = True
    while b_num:
        s_end = s_input[i_pos_check]
        #print(s_end)
        b_num = s_end.isnumeric()
        #print(str(i_pos_check) + " Numeric: " + str(b_num))
        i_pos_check = i_pos_check - 1

    s_left = s_input[0:i_pos_check + 2]
    s_right = s_input[i_pos_check + 2:]

    #print("\nString Starts with [" + s_left + "]")
    #print("String Ends   with [" + s_right + "]")

    return (s_left, s_right)

def get_inc_file_ext(filename):
    newname = ""
    file_name_left_char = ""
    try:
        dot_pos = filename.index(".")
    except ValueError:
        return "?" + filename + " is an invalid file name!"

    file_name_left_char = filename[dot_pos-1]
    try:
        current_num = int(file_name_left_char)
    except:
        current_num = -1
    if current_num == -1:
        newname = filename[0:dot_pos] + "1" + filename[dot_pos:]
    else:
        if current_num != 9:
            newname = filename[0:dot_pos - 1] + str( current_num + 1 ) + filename[dot_pos:]
        else:
            # find total number & increment
            s_split = get_strleft_numright(filename[0:dot_pos])
            # Check for leading 0's
            i_len_num = len(s_split[1])
            if i_len_num > 1:
                i_split_num = 0
                if s_split[1][0] == "0":
                    i_split_num = int("1" + s_split[1])

            # Create New Name1
            if i_split_num > 0:
                i_split_num += 1
                s_split_num0 = str(i_split_num)[1:]
                newname = s_split[0] + s_split_num0 + filename[dot_pos:]
            else:
                newname = s_split[0] + str(int(s_split[1]) + 1) + filename[dot_pos:]


    return newname

