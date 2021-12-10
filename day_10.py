code = open("input_10").readlines()


def score(line):
    # returns (incomplete, corrected) scores
    memory = []
    for c in line:
        if c in '([{<':
            memory.append(c)
            continue
        if c == ")" and memory.pop() != "(":
                return 3, 0
        if c == "]" and memory.pop() != "[":
                return 57, 0
        if c == "}" and memory.pop() != "{":
                return 1197, 0
        if c == ">" and memory.pop() != "<":
                return 25137, 0
    missing = 0
    for m in memory[::-1]:
        missing *= 5
        if m == "(":
            missing += 1
        elif m == "[":
            missing += 2
        elif m == "{":
            missing += 3
        elif m == "<":
            missing += 4
    return 0, missing



scores = [score(l) for l in code]

print(sum(s[0] for s in scores))
completions = [c[1] for c in scores if c[1]]
completions.sort()
print(completions[len(completions)//2])
