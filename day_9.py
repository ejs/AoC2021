from collections import Counter


def neighbours(x, y):
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= x+dx < 100 and 0 <= y+dy < 100:
            yield x+dx, y+dy


world = []

for line in open("input_9"):
    row = [int(c) for c in line.strip()]
    world.append(row)

total_risk = 0
for x, row in enumerate(world):
    for y, point in enumerate(row):
        if all(world[nx][ny] > point for nx, ny in neighbours(x, y)):
            total_risk += point + 1

print(total_risk)

basins = [[-1 if point == 9 else 0 for point in row] for row in world]

next_basin = 1
for x in range(len(basins)):
    for y in range(len(basins[x])):
        if basins[x][y] != 0:
            continue  # either crest or already covered basins
        basins[x][y] = next_basin
        flood = set(neighbours(x, y))
        while flood:
            nx, ny = flood.pop()
            if basins[nx][ny] != 0:
                continue
            basins[nx][ny] = next_basin
            for dx, dy in neighbours(nx, ny):
                flood.add((dx, dy))
        next_basin += 1

basin_sizes = Counter(p for row in basins for p in row)
biggest = [count for n, count in basin_sizes.most_common(4) if n > 0]
print(biggest[0]*biggest[1]*biggest[2])
