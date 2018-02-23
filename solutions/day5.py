def jump(offsets, index):
    val = offsets[index]
    offsets[index] += 1
    new_index = index + val
    try:
        offsets[new_index]
        return offsets, new_index
    except IndexError:
        return None, None

def solve(offsets):
    index = 0
    steps = 0
    while True:
        offsets, index = jump(offsets, index)
        steps += 1
        if not offsets:
            break
    return steps

input = []
with open('inputs/day5.txt') as textfile:
    for line in textfile:
        input.append(int(line))

