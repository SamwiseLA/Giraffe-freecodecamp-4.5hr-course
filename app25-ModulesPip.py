# Use Existing PYTHON files
import useful_tools
import samwise_tools

print("==============================")
dice = input("Enter Number")
print("You Rolled a [" + str(useful_tools.roll_dice(int(dice))) + "] on a " + dice + " sided dice")

file = input("File Name to be incremented, must have .??? format")
fileNew = "?"
while fileNew[0] == "?":
    fileNew = samwise_tools.get_inc_file_ext(file)
    if fileNew[0] != "?":
        print("\nThe Incremendted File Name is: {0}".format(fileNew))
    else:
        print(fileNew[1:])
        file = input("File Name to be incremented, must have .??? format")
exit()

