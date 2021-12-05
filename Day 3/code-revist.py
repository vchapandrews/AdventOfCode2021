import statistics

diagnostic_report = open("diagnostic_report.txt").read().splitlines()

gamma_rate = ""
epsilon_rate = ""
ox_gen_rating = diagnostic_report.copy()
c02_scrub_rating = diagnostic_report.copy()

def empty_trash(input):
    for item in trash:
        input.remove(item)

for column in range(len(diagnostic_report[0])):

    # Calculates gamma and epsilon rates by concatenating column modes/anti-modes
    column_mode = statistics.mode(line[column] for line in diagnostic_report)
    gamma_rate += "1" if column_mode == "1" else "0"
    epsilon_rate += "0" if column_mode == "1" else "1"

    # Works out oxygen generator rating through process of elimination
    if list(line[column] for line in ox_gen_rating).count("1") == list(line[column] for line in ox_gen_rating).count("0"):
        column_mode = "1"
    else:
        column_mode = statistics.mode(line[column] for line in ox_gen_rating)
    trash = [] 
    for line in ox_gen_rating:
        if len(ox_gen_rating) == 1:
            continue
        elif line[column] != column_mode:
            trash.append(line)
    empty_trash(ox_gen_rating)

    # Works out C02 Scrubber rating through process of elimination
    if list(line[column] for line in c02_scrub_rating).count("1") == list(line[column] for line in c02_scrub_rating).count("0"):
        column_mode = "1"
    else:
        column_mode = statistics.mode(line[column] for line in c02_scrub_rating)
    trash = []
    for line in c02_scrub_rating:
        if len(c02_scrub_rating) == 1:
            continue
        elif line[column] == column_mode:
            trash.append(line)
    empty_trash(c02_scrub_rating)

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
life_support = int(ox_gen_rating[0], 2) * int(c02_scrub_rating[0], 2)
print(f"\nPower consumption: {power_consumption}\nLife support: {life_support}\n")
