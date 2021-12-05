import statistics

diagnostic_report = open("diagnostic_report.txt").read().splitlines()

gamma_rate = ""
epsilon_rate = ""
ox_gen_shortlist = diagnostic_report.copy()
c02_scrub_shortlist = diagnostic_report.copy()

def eliminate(input, mode, column):
    column_mode = "1" if list(line[column] for line in input).count("1") == list(line[column] for line in input).count("0") else statistics.mode(line[column] for line in input)
    trash = []
    for line in input:
        if len(input) == 1:
            continue
        elif mode == 1 and line[column] != column_mode:
            trash.append(line)
        elif mode == 2 and line[column] == column_mode:
            trash.append(line)
    for item in trash:
        input.remove(item)

for column in range(len(diagnostic_report[0])):
    column_mode = statistics.mode(line[column] for line in diagnostic_report)
    gamma_rate += "1" if column_mode == "1" else "0"
    epsilon_rate += "0" if column_mode == "1" else "1"
    eliminate(ox_gen_shortlist, 1, column)
    eliminate(c02_scrub_shortlist, 2, column)

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
life_support = int(ox_gen_shortlist[0], 2) * int(c02_scrub_shortlist[0], 2)
print(f"\nPower consumption: {power_consumption}\nLife support: {life_support}\n")