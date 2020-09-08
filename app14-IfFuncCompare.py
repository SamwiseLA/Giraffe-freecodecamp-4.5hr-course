def f_max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(str(f_max_num(int(input("num1: ")),int(input("num2: ")),int(input("num3: ")))) + " is the highest number!")
