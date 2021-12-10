sample = [int(i) for i in open('input_6').readlines()[0].strip().split(',')]
states = [0] * 9

for s in sample:
    states[s] += 1

print(0, states)

for i in range(256):
    new_states = states[1:] + states[:1]
    new_states[6] += states[0]
    states = new_states
    print(i+1, states, sum(states))

print(sum(states))

