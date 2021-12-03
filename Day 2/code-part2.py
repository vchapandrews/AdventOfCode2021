# Starting position of submarine
position = [0, 0, 0]  # [x, y, z] Where x represents the submarine's horizontal position, y represents vertical position, and Z represents aim/angle.
print("Starting Location:", position[:2])

# Functions for modifying location
def up(amount):
    position[2] += amount
def down(amount):
    position[2] -= amount
def forward(amount):
    position[0] += amount
    position[1] += position[2] * amount

# Importing submarine instructions
submarine_instructions = open("Submarine Instructions.txt")

# This splits each line down into a list item, then creates sublists where the first value provides the direction, and the second value provides the distance.
splits_by_line = submarine_instructions.read().splitlines() # ['forward 2', 'forward 2', 'down 7', 'forward 6', 'down 7', 'forward 4', 'down 7', 'up 2', 'forward 4']
for index, instruction in enumerate(splits_by_line):
    splits_by_line[index] = splits_by_line[index].split() # [['forward', '2'], ['forward', '2'], ['down', '7'], ['forward', '6'], ['down', '7'], ['forward', '4'], ['down', '7'], ['up', '2'], ['forward', '4']]  

# Carries out instructions
for sublist_item in splits_by_line:
    if sublist_item[0] == "forward":
        forward(int(sublist_item[1]))
        print("Submarine moved forward",sublist_item[1], "units")
    elif sublist_item[0] == "up":
        up(int(sublist_item[1]))
        print("Submarine angled upwards " + sublist_item[1] + "°")
    elif sublist_item[0] == "down":
        down(int(sublist_item[1]))
        print("Submarine angled downwards " + sublist_item[1] + "°")

# Final position of submarine
print("Final Location:", position[:2])

# Random multiplication exercise to get answer
answer = position[0] * position[1] * -1  # As I've opted to use "y-position" rather than "depth" the polarity of the answer will be inverted unless I multiply by -1.
print("Answer:", answer)