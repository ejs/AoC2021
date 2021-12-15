import heapq
import time


def neighbours(x, y, width, height):
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= x+dx < width and 0 <= y+dy < height:
            yield x+dx, y+dy


def simple_explore(cave):
    costs = [[0 for y in row] for row in cave]
    expand = [(0, (1, 0)), (0, (0, 1))]
    width = len(cave)
    height = len(cave[0])

    while expand:
        # this is the cheapest unexplored route so far
        cost, (x, y) = heapq.heappop(expand)
        if costs[x][y]:
            continue  # already reached by a cheaper route

        # record cost to this point
        new_cost = cave[x][y]+cost
        costs[x][y] = new_cost

        if x == width-1 and y == height-1:
            return new_cost #  reached the exit

        # continue exploring from here
        for nx, ny in neighbours(x, y, width, height):
            if not cave[nx][ny]:
                # don't rexplore points
                heapq.heappush(expand, (new_cost, (nx, ny)))


small_cave = [[int(o) for o in row.strip()] for row in open("input_15")]
now = time.time()
print("small cave", simple_explore(small_cave), time.time()-now)


full_cave = [[(cell+nx+ny-1)%9+1 for ny in range(5) for cell in row] for nx in range(5) for row in small_cave]
now = time.time()
print("large cave", simple_explore(full_cave), time.time()-now)
