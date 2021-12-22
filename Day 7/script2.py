with open("input.txt") as text_file:
    input_data = [int(i) for i in text_file.read().split(",")]

targets_to_try = [i for i in range(min(input_data), max(input_data) + 1)]
position_options = {}

for target in targets_to_try:
    input_data_copy = input_data.copy()
    for idx in range(len(input_data_copy)):
        difference = abs(input_data_copy[idx] - target)
        position_options[target] = position_options.get(target, 0) + sum(range(difference + 1))

best_option = min(position_options, key=position_options.get)

print(f"The most fuel efficient horizontal position is {best_option} which uses {position_options[best_option]} units of fuel.")