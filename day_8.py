from collections import namedtuple


def find_value(display):
    mappings = {}

    for c in display.combinations:
        if len(c) == 2:
            one = c
            mappings[c] = "1"
        elif len(c) == 4:
            four = c
            mappings[c] = "4"
        elif len(c) == 3:
            mappings[c] = "7"
        elif len(c) == 7:
            mappings[c] = "8"

    for c in display.combinations:
        if c in mappings:
            continue  # 1 4 7 8
        if len(c) == 6:
            if all(m in c for m in four):
                nine = c
                mappings[c] = "9"
            elif all(m in c for m in one):
                mappings[c] = "0"
            else:
                mappings[c] = "6"
        elif len(c) == 5:
            if all(m in c for m in one):
                mappings[c] = "3"

    for c in display.combinations:
        if c in mappings:
            continue  # 0 1 3 4 6 7 8 9
        if all(m in nine for m in c):
            mappings[c] = "5"
        else:
            mappings[c] = "2"

    return int("".join(mappings[o] for o in display.outputs))


Display = namedtuple('Display', ['combinations', 'outputs'])
displays = open('input_8').readlines()
displays = [d.partition('|') for d in displays]
displays = [Display(["".join(sorted(i)) for i in c.split()], ["".join(sorted(i)) for i in o.split()]) for c, _, o in displays]


unique = 0
for d in displays:
    for s in d.outputs:
        if len(s) in (2, 3, 4, 7):
            unique += 1
print(unique)

print(sum(find_value(d) for d in displays))
