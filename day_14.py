from collections import defaultdict, Counter
from time import time

def progress_polymer(polymer, rules):
    a = polymer[0]
    extended = a
    for b in polymer[1:]:
        extended += rules.get(a+b) + b
        a = b
    return extended


def recurse_polymer(polymer, rules, depth):
    if not depth:
        yield from polymer
    else:
        a = ""
        for b in recurse_polymer(polymer, rules, depth-1):
            pair = a+b
            if pair in rules:
                yield rules[pair]
            yield b
            a = b

data = open("input_14")

base_polymer = data.readline().strip()
rules = defaultdict(str)


for line in data:
    if not line.strip():
        continue
    pair, _, insert = line.partition('->')
    rules[pair.strip()] = insert.strip()


for j in range(5, 21, 5):
    now = time()
    count = Counter(recurse_polymer(base_polymer, rules, j))
    counts = count.most_common()
    print(j, counts[0][1]-counts[-1][1], time()-now)
