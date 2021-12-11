def neighbours(x, y, width, height):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx or dy) and 0 <= x+dx < width and 0 <= y+dy < height:
                yield x+dx, y+dy


def progress(octopi):
    width = len(octopi)
    height = len(octopi[0])
    new_world = [[o+1 for o in row] for row in octopi]
    flashes = 0
    visit = [(x, y) for x in range(10) for y in range(10) if new_world[x][y] > 9]
    while visit:
        x, y = visit.pop()
        if new_world[x][y] > 9:
            new_world[x][y] = -10
            flashes += 1
            for nx, ny in neighbours(x, y, width, height):
                new_world[nx][ny] += 1
                visit.append((nx, ny))
    new_world = [[max(0, o) for o in row] for row in new_world]

    return new_world, flashes


octopi = [[int(o) for o in row.strip()] for row in open("input_11")]

total_flashes = 0
for i in range(1, 101):
    octopi, flashes = progress(octopi)
    total_flashes += flashes
print(total_flashes)

for i in range(i+1, 1000):
    octopi, flashes = progress(octopi)
    if flashes == 100:
        break
print(i)
