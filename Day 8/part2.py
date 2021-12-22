"""
Okay Part 2 is going to be a lot harder. Potentially I'd start by creating a "letter map" for all the letter number combinations when the wires aren't crossed. I'd do this as a dictionary where the key represents what the letter is supposed to be, and the value represents what the letter is. Or with lists perhaps.

Then there'd be a iteration that checks for the values we know (i.e. 1, 4, 7, and 8) and then reassigns the letters in our letter map accordingly. I think using just these 4 letters we can workout the key map for each segment.

Essentially the letter map will function as a translator.

Then for each output value there will be an iteration that translates the jumbled value into the original unjumbled string (may need to sort alphabetically too) and then there'd be a system that outputs the corresponding number for that string.
"""

with open("input.txt") as text_file:
    input_data = [i.split(" | ") for i in text_file.read().splitlines()]

output_value_sum = 0

for row in input_data:

    letter_map = {"a": "-", "b": "-", "c": "-", "d": "-", "e": "-", "f": "-", "g": "-"}
    value_map = {0: [], 1: 0, 2: [], 3: [], 4: 0, 5: [], 6: [], 7: 0, 8: 0, 9: []}
    display_map = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9} # may not be needed

    for value in row[0].split():

        if len(value) == 2: # i.e. value is 1
            value_map[1] = value

        if len(value) == 4: # i.e. value is 4
            value_map[4] = value

        if len(value) == 3: # i.e. value is 7
            value_map[7] = value

        if len(value) == 7: # i.e. value is 8
            value_map[8] = value

        if len(value) == 5: # i.e. value is 2, 3, or 5
            value_map[2] += [value]
            value_map[3] += [value]
            value_map[5] += [value]
        if len(value) == 6: # i.e. value is 0, 6, or 9
            value_map[0] += [value]
            value_map[6] += [value]
            value_map[9] += [value]

    # ---------------------------------------------------------------------------------
    
    # Works out A

    for letter in value_map[7]:
        if letter in value_map[1]:
            continue
        else:
            letter_map["a"] = letter

    # ---------------------------------------------------------------------------------

    # Works out which value is 9

    trash = []

    for option in value_map[9]:
        for letter in value_map[7] + value_map[4]:
            if letter in option:
                continue
            else:
                trash.append(option)
                break

    if len(trash) > 1: # Clears out other values
        for item in trash:
            value_map[9].remove(item)

    value_map[9] = value_map[9][0]

    # ---------------------------------------------------------------------------------
    
    # Works out which letter is G

    for letter in value_map[9]:
        if letter in value_map[7] + value_map[4]:
            continue
        else:
            letter_map["g"] = letter

    # ---------------------------------------------------------------------------------

    # Works out which value is 3

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

    # ---------------------------------------------------------------------------------

    # Working out D

    for letter in value_map[3]:
        if letter in value_map[7] + letter_map["g"]:
            continue
        else:
            letter_map["d"] = letter

    # ---------------------------------------------------------------------------------

    # Working out B

    for letter in value_map[4]:
        if letter in letter_map["d"] + value_map[1]:
            continue
        else:
            letter_map["b"] = letter

    # ---------------------------------------------------------------------------------

    # Working out 5

    trash = []

    for value in row[0].split():
        if len(value) == 5: # if the value is 5 letters long + the letters for A, B, D and G are there, plus one other letter. That one other letter is F.
            if letter_map["a"] in value and letter_map["b"] in value and letter_map["d"] in value and letter_map["g"] in value:
                value_map[5] = value

    # ---------------------------------------------------------------------------------

    # Working out F

    for letter in value_map[5]:
        if letter in letter_map["a"] + letter_map["b"] + letter_map["d"] + letter_map["g"]:
            continue
        else:
            letter_map["f"] = letter

    # ---------------------------------------------------------------------------------

    # Working out C

    for letter in value_map[1]:
        if letter == letter_map["f"]:
            continue
        else:
            letter_map["c"] = letter

    # ---------------------------------------------------------------------------------

    # Working out E

    for letter in "abcdefg":
        if letter in letter_map.values():
            continue
        else:
            letter_map["e"] = letter

    # ---------------------------------------------------------------------------------

    # Translating output values

    translated_outputs = []

    for output_value in row[1].split():
        translated_output_value = ""
        for i in output_value:
            for letter in letter_map:
                if i == letter_map[letter]:
                    translated_output_value += letter
        translated_outputs.append("".join(sorted(translated_output_value)))

    # ---------------------------------------------------------------------------------

    # Converting translated output values into a 4-digit number (as a string)

    output_value_string = ""

    for i in translated_outputs:
       output_value_string += str(display_map[i])

    # ---------------------------------------------------------------------------------

    # Summing up all 4-digit output numbers

    output_value_sum += int(output_value_string)

print(f"The sum of all values is {output_value_sum}")

"""
Logic thought process:

If the values length is 5, then it represents either 2, 3, or 5.
If the values length is 6, then it represents either 0, 6 or 9.

If we know 5, 6 or 2 then we can work out the positions for c and f.

Decision tree (how to what letter is representing each segment from A-G):
1. A - Compare the value that is 3 digits long with the value that is 2 digits long. The outlying number represents the A segment.
2. G - We know our number is 9 if it has all the letters from 7 and from 4, plus one additional letter. That one additional letter represents our G segment.
3. D - 3 has all the letters from 7, plus our G segment letter, plus one other letter. That one other letter is D.
4. B - B is the letter in 4 that is not used to represent the D segment and is not a letter in 1.
5. F - if the value is 5 letters long + the letters for A, B, D and G are there, plus one other letter. That one other letter is F.
6. C - Once we have F, we can deduce what C is.
7. E - This will be the remaining letter.
"""