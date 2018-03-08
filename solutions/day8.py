from operator import gt, lt, ge, le, eq, ne
import re



def evaluate_condition(condition, registers):
    p = re.compile(r'(\w+)\s(.*)\s(-*\d+)')
    reg, symbol, val = p.search(condition).groups()
    operator_map = {
        '>': gt,
        '<': lt,
        '>=': ge,
        '<=': le,
        '==': eq,
        '!=': ne
    }
    operator = operator_map.get(symbol)
    reg_val = registers.setdefault(reg, 0)
    return operator(reg_val, int(val))

def parse_instruction(instruction):
    p = re.compile(r'(\w+)\s(dec|inc)\s(-*\d+)\sif\s(.*)')
    reg, modifier, val, condition = p.search(instruction).groups()
    val = int(val)
    if modifier == 'dec':
        val *= -1
    return reg, val, condition

def update_register(reg, val, registers):
    registers[reg] += val
    return registers

def process_instruction(instruction, registers):
    reg, val, condition = parse_instruction(instruction)
    eval = evaluate_condition(condition, registers)
    registers.setdefault(reg, 0)
    if eval:
        update_register(reg, val, registers)
    return registers

def solve(instructions):
    registers = {}
    for instruction in instructions:
        registers = process_instruction(instruction, registers)
    return max(registers.values())

