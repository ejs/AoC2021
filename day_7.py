sample = [int(i) for i in open('input_7').readlines()[0].strip().split(',')]
row = [0] * (max(sample)+1)

for c in sample:
    row[c] += 1

lowest_cost = max(sample)*max(sample)
for x in range(max(sample)):
    cost = sum(abs(i-x)*c for i, c in enumerate(row))
    if cost < lowest_cost:
        print(x, cost)
        lowest_cost = cost

def full_cost(a, b):
    distance = abs(a-b)
    return distance*(distance+1)//2

lowest_cost = max(sample)*max(sample)*max(sample)
for x in range(max(sample)):
    cost = sum(full_cost(x, i)*c for i, c in enumerate(row))
    if cost < lowest_cost:
        print(x, cost)
        lowest_cost = cost
