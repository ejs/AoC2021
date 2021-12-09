history = []
local_increases = 0
smoothed_increases = 0

for depth in (int(l) for l in open("input_1")):
    if history:
        if depth > history[-1]:
            local_increases += 1
        if len(history) == 3:
            if depth > history[0]:
                smoothed_increases += 1
    history.append(depth)
    history = history[-3:]
print(local_increases)
print(smoothed_increases)
