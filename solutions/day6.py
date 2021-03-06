class Bank(object):
    def __init__(self, banks):
        self.banks = banks
        self.history = [banks[:]]

    def add_block(self, index):
        try:
            self.banks[index] += 1
            index += 1
        except IndexError:
            self.banks[0] += 1
            index = 1
        return index

    def remove_blocks(self):
        max_blocks = max(self.banks)
        index = self.banks.index(max_blocks)
        blocks = self.banks[index]
        self.banks[index] = 0
        return blocks, index

    def distribute_blocks(self):
        blocks, index = self.remove_blocks()
        index += 1
        while blocks > 0:
            index = self.add_block(index)
            blocks -= 1

    def is_repeat_state(self):
        if self.banks in self.history:
            return True
        return False

    def cycles(self):
        return len(self.history)

    def reallocate_blocks(self):
        while True:
            self.distribute_blocks()
            if self.is_repeat_state():
                break
            self.history.append(self.banks[:])
        return self.banks

    def solve(self):
        self.reallocate_blocks()
        return self.cycles()

with open('inputs/day6.txt') as textfile:
    input = textfile.read().split()

