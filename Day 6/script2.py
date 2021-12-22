
'''
The problem now is that because the population is growing exponentially, the processing requirements are now to high for the old modelling system to work. Had to get hints online, but the idea is to use a new modelling system that represents the population different. Instead of each fish being represented by a number in a list, instead there are only 9 numbers in the list that represent the number of fish at each state in their lifecycle. It's the same data, just presented differently.
'''

with open("input.txt") as text_file:
    input_data = [int(i) for i in text_file.read().split(",")]

fishstates = [0]*9

for i in input_data:
    for state in range(9):
        if i == state:
            fishstates[state] += 1

duration = 256

for day in range(0, duration):
    newfishstates = [0]*9
    for idx in range(8,-1,-1):
        if idx == 0:
            newfishstates[6] += fishstates[0]
            newfishstates[8] += fishstates[0] if fishstates[0] > 0 else 0
        else:
            newfishstates[idx - 1] = fishstates[idx]
    fishstates = newfishstates

population = sum([i for i in fishstates])
print(f"After {duration} days, there are {population} lanternfish.")