"""
1. Process input data so that the Unique Signal Patterns are separated from the Output values.
2. Looking at just the output values, count how many times a value with a length of 2, 3, 4, or 7 comes up.
"""

with open("input.txt") as text_file:
    input_data = [i.split(" | ") for i in text_file.read().splitlines()]

output_values = [i[1].split() for i in input_data]

answer = 0
for row in output_values:
    for value in row:
        if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
            answer += 1

print(answer)