is_male = False

if is_male:
    print("He is Male")
else:
    print("She is Female")


valid_num = False

while not valid_num:
    output_msg = " is greater than 10"
    amt = int(input("Enter number 1-10: "))
    if amt < 1:
        output_msg = " is less than 1"
    elif 0 < amt < 6:
        output_msg = " is between 1 and 5"
        valid_num = True
    elif 5 < amt < 11:
        output_msg = " is between 6 and 10"
        valid_num = True

    print("\n" + str(amt) + output_msg)
    if not valid_num:
        print("========>\nINVALID NUMBER - PLEASE TRY AGAIN!\n<========")

print("\nThanks For Playing")
