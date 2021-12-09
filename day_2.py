aim = 0
correct_depth = 0
simple_depth = 0
horizontal = 0

for command, _, distance in (l.partition(' ') for l in open("input_2")):
    distance = int(distance)
    if command == "forward":
        horizontal += distance
        correct_depth += aim*distance
    elif command == "down":
        simple_depth += distance
        aim += distance
    elif command == "up":
        simple_depth -= distance
        aim -= distance
print("simple", simple_depth*horizontal)
print("correct", correct_depth*horizontal)
