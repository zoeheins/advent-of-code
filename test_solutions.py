import unittest
from solutions import *

class TestDayOne(unittest.TestCase):

    def test_returns_sum(self):
        result = day1.solve('1122')
        self.assertEqual(result, 3)

    def test_returns_zero(self):
        result = day1.solve('1234')
        self.assertEqual(result, 0)


class TestDayFour(unittest.TestCase):

    def test_returns_valid(self):
        self.assertTrue(day4.is_valid('aa bb cc dd ee'))

    def test_return_false(self):
        self.assertFalse(day4.is_valid('aa bb cc dd aa'))

    def test_solve_return_total_valid(self):
        input = ['aa aa', 'bb cc', 'dd dd']
        result = day4.solve(input)
        self.assertEqual(result, 1)


class TestDayFive(unittest.TestCase):

    def test_jump_increases_offset(self):
        offsets = day5.jump([0, 3, 0, 1, -3], 0)
        self.assertEqual(offsets, ([1, 3, 0, 1, -3], 0))

    def test_jumps_moves_backwards(self):
        offsets = day5.jump([2, 4, 0, 1, -3], 4)
        self.assertEqual(offsets, ([2, 4, 0, 1, -2], 1))

    def test_jump_returns_none_when_lands_outside(self):
        offsets = day5.jump([2, 4, 0, 1, -2], 1)
        self.assertEqual(offsets, (None, None))

    def test_solve_returns_total_step(self):
        self.assertEqual(5, day5.solve([0, 3, 0, 1, -3]))


class TestDaySix(unittest.TestCase):

    def setUp(self):
        self.bank = day6.Bank([7, 1, 0, 7])

    def test_history_is_list_of_banks(self):
        self.assertEqual(self.bank.history, [[7, 1, 0 ,7]])

    def test_remove_blocks_returns_max_blocks_and_index(self):
        result = self.bank.remove_blocks()
        self.assertEqual(result, (7, 0))

    def test_remove_blocks_sets_max_memory_bank_to_zero(self):
        self.bank.remove_blocks()
        self.assertEqual(self.bank.banks, [0, 1, 0, 7])

    def test_add_block_increases_block(self):
        self.bank.add_block(0)
        self.assertEqual(self.bank.banks, [8, 1, 0, 7])

    def test_add_block_loops_to_start(self):
        index = self.bank.add_block(4)
        self.assertEqual(self.bank.banks, [8, 1, 0, 7])
        self.assertEqual(index, 1)

    def test_distribute_blocks(self):
        bank = day6.Bank([0, 2, 7, 0])
        bank.distribute_blocks()
        self.assertEqual(bank.banks, [2, 4, 1, 2])
        bank.distribute_blocks()
        self.assertEqual(bank.banks, [3, 1, 2, 3])

    def test_reallocate_blocks_stop_when_hit_repeat_pattern(self):
        bank = day6.Bank([0, 2, 7, 0])
        bank.reallocate_blocks()
        self.assertEqual(bank.banks, [2, 4, 1, 2])
        self.assertEqual(bank.cycles(), 5)

    def test_count_cycles_returns_total_iterations(self):
        bank = day6.Bank([0, 2, 7, 0])
        bank.reallocate_blocks()
        self.assertEqual(bank.cycles(), 5)

    def test_solve_returns_total_cycles(self):
        bank = day6.Bank([0, 2, 7, 0])
        self.assertEqual(bank.solve(), 5)
