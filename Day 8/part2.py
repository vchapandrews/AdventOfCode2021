with open("input.txt") as text_file:
    input_data = [i.split(" | ") for i in text_file.read().splitlines()]

output_value_sum = 0

for row in input_data:

    letter_map = {"a": "-", "b": "-", "c": "-", "d": "-", "e": "-", "f": "-", "g": "-"}
    value_map = {0: [], 1: 0, 2: [], 3: [], 4: 0, 5: [], 6: [], 7: 0, 8: 0, 9: []}
    display_map = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9} # may not be needed

    for value in row[0].split():
        if len(value) == 2:
            value_map[1] = value
        if len(value) == 4:
            value_map[4] = value
        if len(value) == 3:
            value_map[7] = value
        if len(value) == 7:
            value_map[8] = value
        if len(value) == 5:
            value_map[2] += [value]
            value_map[3] += [value]
            value_map[5] += [value]
        if len(value) == 6:
            value_map[0] += [value]
            value_map[6] += [value]
            value_map[9] += [value]

    for letter in value_map[7]:
        if letter in value_map[1]:
            continue
        else:
            letter_map["a"] = letter

    trash = []
    for option in value_map[9]:
        for letter in value_map[7] + value_map[4]:
            if letter in option:
                continue
            else:
                trash.append(option)
                break
    if len(trash) > 1:
        for item in trash:
            value_map[9].remove(item)
    value_map[9] = value_map[9][0]

    for letter in value_map[9]:
        if letter in value_map[7] + value_map[4]:
            continue
        else:
            letter_map["g"] = letter

    trash = []
    for option in value_map[3]:
        for letter in value_map[7] + letter_map["g"]:
            if letter in option:
                continue
            else:
                trash.append(option)
                break
    if len(trash) > 1:
        for item in trash:
            value_map[3].remove(item)
    value_map[3] = value_map[3][0]

    for letter in value_map[3]:
        if letter in value_map[7] + letter_map["g"]:
            continue
        else:
            letter_map["d"] = letter

    for letter in value_map[4]:
        if letter in letter_map["d"] + value_map[1]:
            continue
        else:
            letter_map["b"] = letter

    trash = []
    for value in row[0].split():
        if len(value) == 5:
            if letter_map["a"] in value and letter_map["b"] in value and letter_map["d"] in value and letter_map["g"] in value:
                value_map[5] = value

    for letter in value_map[5]:
        if letter in letter_map["a"] + letter_map["b"] + letter_map["d"] + letter_map["g"]:
            continue
        else:
            letter_map["f"] = letter

    for letter in value_map[1]:
        if letter == letter_map["f"]:
            continue
        else:
            letter_map["c"] = letter

    for letter in "abcdefg":
        if letter in letter_map.values():
            continue
        else:
            letter_map["e"] = letter

    translated_outputs = []
    for output_value in row[1].split():
        translated_output_value = ""
        for i in output_value:
            for letter in letter_map:
                if i == letter_map[letter]:
                    translated_output_value += letter
        translated_outputs.append("".join(sorted(translated_output_value)))

    output_value_string = ""
    for i in translated_outputs:
       output_value_string += str(display_map[i])

    output_value_sum += int(output_value_string)

print(f"The sum of all values is {output_value_sum}")
