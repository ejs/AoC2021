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

    to_flash = {(x, y) for x, row in enumerate(new_world) for y, o in enumerate(row) if o > 9}
    while to_flash:
        x, y = to_flash.pop()
        flashes += 1
        for nx, ny in neighbours(x, y, width, height):
            if new_world[nx][ny] == 0:
                continue
            new_world[nx][ny] += 1
            if new_world[nx][ny] > 9 :
                to_flash.add((nx, ny))
        new_world[x][y] = 0

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
