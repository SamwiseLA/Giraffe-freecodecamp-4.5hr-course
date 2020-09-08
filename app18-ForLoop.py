# For Loops parse the "in" value,
# and set the "for" variable to each parsed item
# until all parsed values have been used
#
s_friends = ["?", "Marta", "Scott C", "Scott N", "Rocky", "Tina"]
s_friends_lower = s_friends.copy()
s_string = input("Enter String?: ")
s_leading_spaces = ""
s_look_for = ""
#
# Convert entire list to lowercase to search later
#
i_index = 0
for s_friend in s_friends:
    s_friends_lower[i_index] = s_friend.lower()
    i_index += 1

#
# Loop each letter in a text string
#
print("===> Loop Entered Value")
for s_letter in s_string:
    print(s_letter)
#
# Loop a List of items in a list
#
print("===> Loop List Items " + str(s_friends))
for s_name in s_friends:
    print(s_name)
#
# Loop a range of of numbers - From first to -1 last
#
print("===> Loop Range 6 to 12")
for i_index in range(6, 12):
    s_leading_spaces = ""
    for i_current in range(i_index):
        s_leading_spaces = s_leading_spaces + " "
    print(s_leading_spaces + str(i_index))

#
# Loop a range of numbers - From first(0) to -1 LAST ITEM IN LIST!!!
#
print("===> Loop List Items with Range " + str(s_friends))
for i_index in range(len(s_friends)):
    print(str(i_index) + ": " + s_friends[i_index])

#
# Loop a range items in a list - From found item to end
# if can't find item, ask again
# search item converted to lowercase (see above) & list examined converted
# to copy of original list in lowercase version
#
print(s_friends)
i_friend_found = 0
while i_friend_found == 0:
    s_look_for = input("Look Starting With: ")
    if s_look_for.lower() in s_friends_lower:
        i_friend_found = s_friends_lower.index(s_look_for.lower())
    else:
        i_friend_found = 0

print("===> Loop List Items with Range " + str(s_friends) + " starting with " + s_look_for)
for i_index in range(i_friend_found, len(s_friends)):
    print(str(i_index) + ": " + s_friends[i_index])
