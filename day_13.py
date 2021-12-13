code = open("input_13")

paper = set()
for line in iter(code.readline, "\n"):
    x, _, y = line.strip().partition(',')
    paper.add((int(x), int(y)))
print(len(paper))


for fold in code:

    instruction, _, line = fold.strip().partition("=")
    if instruction[-1] == "x":
        x_line, y_line = int(line), 2000
    elif instruction[-1] == "y":
        x_line, y_line = 2000, int(line)

    folded = set()
    for x, y in list(paper):
        ny = 2*y_line-y if y > y_line else y
        nx = 2*x_line-x if x > x_line else x
        folded.add((nx, ny))
    paper = folded

    print(len(paper))

for y in range(max(y for (x, y) in paper)+1):
    print("".join("•" if (x, y) in paper else " " for x in range(max(x for (x, y) in paper)+1)))
