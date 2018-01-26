with open('inputs/day4.txt') as textfile:
    input = textfile.read().splitlines()

def is_valid(passphrase):
    words = passphrase.split()
    if len(words) == len(set(words)):
        return True
    return False

def solve(phrases):
    return len([phrase for phrase in phrases if is_valid(phrase)])
