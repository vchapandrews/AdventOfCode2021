# This program looks at the values in SonarMeasurements.txt and counts how many times a value increased (compared to the value before it.)

measurements_doc = open("SonarMeasurements.txt", "r")

list_of_measurements = measurements_doc.read().splitlines()

depth_increases = 0

for index, measurement in enumerate(list_of_measurements):
    if int(list_of_measurements[index]) == 0:
        continue
    elif int(list_of_measurements[index]) > int(list_of_measurements[index - 1]):
        print(list_of_measurements[index])
        depth_increases += 1
    
print("Total number of depth increases:", depth_increases)