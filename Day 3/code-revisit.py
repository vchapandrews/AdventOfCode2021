import statistics

diagnostic_report = open("diagnostic_report.txt").read().splitlines()

gamma_rate = ""
epsilon_rate = ""

bit_length = 12

ox_gen_shortlist = diagnostic_report.copy()
c02_shortlist = diagnostic_report.copy()

for column in range(bit_length):
    
    # Gamma rate calculator
    temp_list = []
    for number in diagnostic_report:
        temp_list.append(number[column])
    gamma_rate += str(statistics.mode(temp_list))
    
    # Epsilon rate calculator
    temp_list = []
    for number in diagnostic_report:
        temp_list.append(number[column])
    if int(statistics.mode(temp_list)) == 1:
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"
 
    temp_list = []
    to_be_deleted = []

    # Oxygen generator rating calculator
    for number in ox_gen_shortlist:
        temp_list.append(number[column])
    column_mode = str(statistics.mode(temp_list))
    if len(ox_gen_shortlist) == 1:
        ox_gen_rating = ox_gen_shortlist[0]
    elif temp_list.count("0") == temp_list.count("1"):
        for number in ox_gen_shortlist:
            if number[column] != "1":
                to_be_deleted.append(number)
    else:
        for number in ox_gen_shortlist:  
            if number[column] != column_mode:
                to_be_deleted.append(number)
    for items in to_be_deleted:
        ox_gen_shortlist.remove(items)

    to_be_deleted = []

    # C02 Scrubber Rating Calculator
    print(f"\n\nC02 Round {column + 1}:",c02_shortlist)
    print(f"Column mode: {column_mode}")
    if len(c02_shortlist) == 1:
        c02_scrubber_rating = c02_shortlist[0]
    elif temp_list.count("0") == temp_list.count("1"):
        for number in c02_shortlist:
            if number[column] != "0":
                to_be_deleted.append(number)
    else:
        for number in c02_shortlist:  
            if int(number[column]) == int(column_mode):
                to_be_deleted.append(number)
    for items in to_be_deleted:
        c02_shortlist.remove(items)

    
ox_gen_rating = ox_gen_shortlist[0]
c02_scrubber_rating = c02_shortlist[0]

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
ox_gen_rating = convert_to_decimal(ox_gen_rating)
c02_scrubber_rating = convert_to_decimal(c02_scrubber_rating)

print(f"Gamma rate is {gamma_rate}, Epsilon rate is {epsilon_rate}, Oxygen Generator rating is {ox_gen_rating}, and C02 Scrubber Rating is {c02_scrubber_rating}.")

power_consumption = gamma_rate * epsilon_rate
life_support = ox_gen_rating * c02_scrubber_rating

print(f"Power consumption is: {power_consumption}\nLife support is: {life_support}.")