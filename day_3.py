ones = [0]*12
count = 0

lines = list(open("input_3"))
for l in lines:
    count += 1
    for i, b in enumerate(l):
        if b == "1":
            ones[i] += 1
gamma = "".join("1" if c > count/2 else "0" for c in ones)
epsilon = "".join("1" if c < count/2 else "0" for c in ones)
print(int(gamma, 2) * int(epsilon, 2))

oxygen = lines[:]
for i in range(len(oxygen[0])):
    ones = sum(1 for v in oxygen if v[i] == "1")
    most_common = "1" if ones >= len(oxygen)/2 else "0"
    oxygen = [l for l in oxygen if l[i] == most_common]
    if len(oxygen) == 1:
        oxygen = oxygen[0]
        break
print(oxygen)

co2 = lines[:]
for i in range(len(co2[0])):
    ones = sum(1 for v in co2 if v[i] == "1")
    most_common = "1" if ones >= len(co2)/2 else "0"
    co2 = [l for l in co2 if l[i] != most_common]
    if len(co2) == 1:
        co2 = co2[0]
        break
print(co2)

print(int(oxygen, 2) * int(co2, 2))
