from collections import namedtuple

Line = namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])

lines = []
for line in open('input_5'):
    start, _, end = line.partition('->')
    x1, _, y1 = start.partition(',')
    x2, _, y2 = end.partition(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    # always go left
    if x1 < x2:
        lines.append(Line(x1, y1, x2, y2))
    else:
        lines.append(Line(x2, y2, x1, y1))

world = [[0]*1000 for i in range(1000)]
for line in lines:
    if line.x1 == line.x2:
        for y in range(min(line.y1, line.y2), max(line.y1, line.y2)+1):
            world[line.x1][y] += 1
    if line.y1 == line.y2:
        for x in range(min(line.x1, line.x2), max(line.x1, line.x2)+1):
            world[x][line.y1] += 1
print(sum(1 for row in world for cell in row if cell > 1))

for line in lines:
    if line.x1 == line.x2:
        continue
    if line.y1 == line.y2:
        continue
    if line.y1 < line.y2:
        direction = 1
    else:
        direction = -1
    for x, y in enumerate(range(line.y1, line.y2+direction, direction), start=line.x1):
        world[x][y] += 1
print(sum(1 for row in world for cell in row if cell > 1))
