def fold(point, line):
    return 2*line-point if point > line else point


code = (l.strip() for l in open("input_13"))

# fill starting dots
paper = set()
for line in code:
    if not line:
        break
    x, _, y = line.partition(',')
    paper.add((int(x), int(y)))


# follow fold instructions
for instruction in code:

    # this puts a virtual fold far off the paper on the other side
    # to simplify the later folding logic
    description, _, line = instruction.partition("=")
    if description[-1] == "x":
        x_line, y_line = int(line), 2000
    elif description[-1] == "y":
        x_line, y_line = 2000, int(line)

    paper = {(fold(x, x_line), fold(y, y_line)) for x, y in paper}
    print(len(paper))

# display final state
for y in range(max(y for (x, y) in paper)+1):
    for x in range(max(x for (x, y) in paper)+1):
        print("•" if (x, y) in paper else " ", end="")
    print()
