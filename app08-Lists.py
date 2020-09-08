from typing import List

friends: List[str] = ["Marta", "Scott N", "Scott C", "Wink", "Czaba", "Mitch", "Julian"]

print("Friend List")
print(friends)
print("===========")
print("=== Indexd 0 ===")
print(friends[0])
print("==== loop through friends ====")
for x in friends:
    print(x)
print("How Many Friends")
print(len(friends))

print("Wink is number " + str(friends.index("Wink") + 1) + " in the list")