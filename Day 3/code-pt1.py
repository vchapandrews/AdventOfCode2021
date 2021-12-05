import statistics

diagnostic_report = open("diagnostic_report.txt").read().splitlines()

gamma_rate = ""
epsilon_rate = ""

for column in range(12):
    # Gamma rate calculator
    temp_list = []
    for number in diagnostic_report:
        temp_list.append(number[column])
    gamma_rate += str(statistics.mode(temp_list))
    temp_list = []
    # Epsilon rate calculator
    for number in diagnostic_report:
        temp_list.append(number[column])
    if int(statistics.mode(temp_list)) == 1:
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

print(f"Gamma rate is {gamma_rate}, Epsilon rate is {epsilon_rate}")

# This function converts binary (strings) to decimal (integer). There's probs a library module that can do this, but for learning purposes will do from scratch.
def convert_to_decimal(input):
    decimal_number = 0
    power = 0
    for digit in input[::-1]:
        decimal_number += int(digit) * (2 ** power)
        power += 1
    return decimal_number

gamma_rate = convert_to_decimal(gamma_rate)
epsilon_rate = convert_to_decimal(epsilon_rate)

print(f"Gamma rate is {gamma_rate}, Epsilon rate is {epsilon_rate}")

power_consumption = gamma_rate * epsilon_rate

print(f"Power consumption is: {power_consumption}")