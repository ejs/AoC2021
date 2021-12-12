from collections import defaultdict
from copy import copy


def explore(start, cave, visited=set()):
    if start.lower() == start:
        visited = copy(visited)
        visited.add(start)
    for edge in cave[start]:
        if edge == "end":
            # reached the end
            yield [edge, start]
            continue
        if edge in visited:
            continue # can't revisit
        # continue exploring
        for path in explore(edge, cave, visited):
            path.append(start)
            yield path


def long_explore(start, cave, visited=set()):
    small_cave = (start.lower() == start)

    if small_cave:
        full_visited = copy(visited)
        full_visited.add(start)
    else:
        full_visited = visited

    for edge in cave[start]:
        if edge == "end":
            # reached the end
            yield [edge, start]
            continue
        if edge in full_visited:
            continue # can't revisit
        for path in long_explore(edge, cave, full_visited):
            path.append(start)
            yield path
        if small_cave:
            # continue allowing revisiting this cave once
            for path in explore(edge, cave, visited):
                path.append(start)
                yield path


grid = defaultdict(set)

for edge in open("input_12"):
    start, _, end = edge.strip().partition('-')
    if not (end == "start" or start == "end"):
        grid[start].add(end)
    if not (start == "start" or end == "end"):
        grid[end].add(start)


print(sum(1 for _ in explore('start', grid)))

# have to dedupe the paths as we could have skipped a cave two ways
print(len(set(tuple(p) for p in long_explore('start', grid))))
