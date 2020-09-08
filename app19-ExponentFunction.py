# Exponent Function

def f_raise_to_power(ni_1, ii_2):
    n_value = 1.0
    for i in range(ii_2):
        n_value = n_value * ni_1

    return n_value

n_1 = ''

while n_1 != "x":
    n_1 = ""
    b_float = False
    print("Please enter Number and Power, \"x\" to Quit")
    while not n_1.isnumeric() and not b_float and n_1 != "x":
        n_1 = input("num 1: ")
        try:
            f_1 = n_1
            f_1 = float(f_1)
            b_float = True
        except ValueError:
            n_1 = n_1

    i_2 = ""
    while not i_2.isdecimal() and (n_1 != "x" and i_2 != "x"):
        i_2 = input("num 2: ")
    if n_1 != "x" and i_2 != "x":
        print("[{0}] to the Power of [{1}]: [{2:,}]\n".format(n_1, i_2, f_raise_to_power(float(n_1), int(i_2))))

print("\n***Exponential Calculator Ended***\n***      Have a nice day       ***\n**********************************")
