b_valid = False

while not b_valid:
    try:
        number = int(input("Enter Number: " ))
        b_valid = True
        print ("\nYour number is {0:,}".format(number))
    except ValueError as err:
        print("!!! Invalid Entry: " + str(err) + "!!!")

print("*** Program Ended Successfully ***")