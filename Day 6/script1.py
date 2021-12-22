
'''
There will be a list that contains all the lanternfish, represented by their current position in the 7 day life-cycle. Everytime a lanternfish's life cycle reaches zero, it resets to 6 and appends a new lanternfish with a value of 8 to the list.

Needs to be some sort of loop system that iterates through each item in the list and subtracts 1 from each value - UNLESS it's at 0, in which case it sets the lifecycle to 6 and appends an 8 too.
'''

with open("input.txt") as text_file:
    input_data = [int(i) for i in text_file.read().split(",")]

duration = 80

print(f"Day 0: {input_data}")
for day in range(0, duration):
    for idx in range(len(input_data)):
        if input_data[idx] == 0:
            input_data[idx] = 6
            input_data.append(8)
        else:
            input_data[idx] -= 1
    print(f"Day {day + 1}: {input_data}")

print(f"After {duration} days, there are {len(input_data)} lanternfish.")