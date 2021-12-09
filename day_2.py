depth = 0
horizontal = 0

for command, _, distance in (l.partition(' ') for l in open("input_2")):
    distance = int(distance)
    if command == "forward":
        horizontal += distance
    elif command == "down":
        depth += distance
    elif command == "up":
        depth -= distance
print("simple", depth*horizontal)


depth = 0
horizontal = 0
aim = 0
for command, _, distance in (l.partition(' ') for l in open("input_2")):
    distance = int(distance)
    if command == "forward":
        horizontal += distance
        depth += aim*distance
    elif command == "down":
        aim += distance
    elif command == "up":
        aim -= distance
print("simple", depth*horizontal)
