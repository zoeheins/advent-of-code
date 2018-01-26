with open('inputs/day2.txt', 'r') as textfile:
    input = textfile.read().rstrip().split('\n')
    input_array = [i.split() for i in input]

def solve(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        row = [int(i) for i in row]
        checksum += max(row) - min(row)
    return checksum

print(solve(input_array))

