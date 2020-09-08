lucky_nums = [1, 4, 23, 54, 76, 23, 8756, 43]
friends = ["Marta", "Scott N", "Scott C", "Wink", "Czaba", "Mitch", "Julian"]

print(friends)
print(len(friends))

print(lucky_nums)

friends.extend(lucky_nums)

print(friends)
print(len(friends))

friends.append("Jack")

print(friends)
print(len(friends))

friends.insert(3, "Tom")

print(friends)
print(len(friends))

friends.remove(1)

print(friends)
print(len(friends))

friends.remove(4)
friends.remove(23)
friends.remove(54)
friends.remove(76)
friends.remove(23)
friends.remove(8756)
friends.remove(43)

print("=== sort ===")
friends.sort()
lucky_nums.sort()

print(friends)
friends.reverse()
print(friends)
print(len(friends))
print(lucky_nums)
lucky_nums.reverse()
print(lucky_nums)
print(len(lucky_nums))


#SET (=) just points at Memory
#Copy creates a copy of the data
print("---> If you just use =, it points at the data, so if you change the old data, if also changes the new data")
print("---> If you just use copy(), it creates new data concatainer, so if you change the old data, if WON'T effect the new data")
friends2 = friends

print(friends)
print(friends2)
friends[0] = "?"
print("---> Change 0 index")
print(friends)
print(friends2)
print("")
print("---> Copy")
print("")
friends3 = friends2.copy()
print(friends2)
print(friends3)
friends2[0] = "W"
print("---> Change 0 index")
print(friends2)
print(friends3)
