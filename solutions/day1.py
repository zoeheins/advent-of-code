with open('inputs/day1.txt', 'r') as textfile:
    input = textfile.read().rstrip()

def solve(input):
    sequence = [int(i) for i in list(input)]
    sum = 0

    for index, digit in enumerate(sequence):
        try:
            next_digit = sequence[index + 1]
        except IndexError:
            next_digit = sequence[0]
        if digit == next_digit:
            sum += digit
    return sum
