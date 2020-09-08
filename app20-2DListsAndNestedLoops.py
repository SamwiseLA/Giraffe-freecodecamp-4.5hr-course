number_list = [
    1, 2, 3, 4, 5
]

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_list)

i_hold = 0
for i in number_list:
    i_hold = i_hold + i
    print(str(i) + ": " + str(i_hold))

print(number_grid[0])
print(number_grid[1])
print(number_grid[2])


print("\nFrom Grid - [1][1]")
print(number_grid[1][1])

print("========================")

for row in number_grid:
    print(row)
    for col in row:
        print(col)
