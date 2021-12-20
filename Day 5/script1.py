with open("input_text.txt") as input_text:
    input_data = input_text.read()

input_coor = [i.split(" -> ") for i in input_data.splitlines()]

for idx in range(len(input_coor)):
    input_coor[idx][0] = input_coor[idx][0].split(",")
    input_coor[idx][1] = input_coor[idx][1].split(",")
    for i in input_coor[idx]:
        i[0] = int(i[0])
        i[1] = int(i[1])

coor_congestion = {}

for idx in range(len(input_coor)):

    x1 = input_coor[idx][0][0]
    x2 = input_coor[idx][1][0]
    y1 = input_coor[idx][0][1]
    y2 = input_coor[idx][1][1]

    if x1 == x2 or y1 == y2: # I.e. Horizontal and vertical lines ONLY

        if x1 > x2: # Plots horizontal lines
            for i in range(x2, x1 + 1):
                coor_congestion[i, y2] = coor_congestion.get((i, y2), 0) + 1
        elif x2 > x1:
            for i in range(x1, x2 + 1):
                coor_congestion[i, y2] = coor_congestion.get((i, y2), 0) + 1
        
        if y1 > y2: # Plots vertical lines
            for i in range(y2, y1 + 1):
                coor_congestion[x1, i] = coor_congestion.get((x1, i), 0) + 1
        elif y2 > y1:
            for i in range(y1, y2 + 1):
                coor_congestion[x1, i] = coor_congestion.get((x1, i), 0) + 1
    
    else: # Diagonal lines ONLY
        
        coor_congestion[x1, y1] = coor_congestion.get((x1, y1), 0) + 1
        direction = int((x2 - x1) / abs(x2 - x1))

        if (x2 > x1 and y2 > y1) or (x2 < x1 and y2 < y1): # i.e. y = x + c
            c = y2 - x2
            while x1 != x2:
                x1 += direction
                y1 = x1 + c
                coor_congestion[x1, y1] = coor_congestion.get((x1, y1), 0) + 1
        
        elif (x2 > x1 and y2 < y1) or (x2 < x1 and y2 > y1): # i.e. y = -x + c
            c = y2 + x2
            while x1 != x2:
                x1 += direction
                y1 = -x1 + c
                coor_congestion[x1, y1] = coor_congestion.get((x1, y1), 0) + 1
    
overlaps = 0
for key in coor_congestion:
    overlaps += 1 if coor_congestion[key] > 1 else 0
print(f"There are {overlaps} points where lines overlap.")