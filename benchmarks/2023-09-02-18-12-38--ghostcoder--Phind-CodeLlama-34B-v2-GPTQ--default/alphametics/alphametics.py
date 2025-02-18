from collections import defaultdict
import re
def solve(puzzle):
    words = re.findall(r'\D+|\d+', puzzle)
    non_digits = [word for word in words if not word.isdigit()]
    digits = [word for word in words if word.isdigit()]

    chars = set(''.join(non_digits))
    num_chars = len(chars)

    if num_chars > 10: # there are at most 10 distinct digits in single-digit numbers
        return None

    for config in generate_configurations(chars):
        try:
            mapping = make_mapping(non_digits, config)
            left = eval_equation(mapping, *parse_equation(words[0]))
            right = eval_equation(mapping, *parse_equation(words[2]))

            if left + right == eval_equation(mapping, *parse_equation(words[4])):
                return {chr(i+ord('A')) if chr(i+ord('A')) in mapping else i: mapping[i] for i in range(num_chars)}
        except ValueError:
            pass

    return None

def parse_equation(eq):
    eq = eq.replace(" ", "")
    plus = eq.find('+')
    if plus >= 0:
        return (int(eq[:plus]), int(eq[plus+1:]))
    else:
        return (int(eq), )

def eval_equation(mapping, a, b=None):
    if b is not None:
        return a - b
    else:
        return a

def make_mapping(words, config):
    mapping = {}
    for word in words:
        for c in word:
            if c not in mapping:
                mapping[c] = config.pop(0) # Changed from config[len(mapping)]
    return mapping

def generate_configurations(chars):
    num_chars = len(chars)
    for bits in range(1 << num_chars):
        yield [digit for digit in range(num_chars) if bits & (1 << digit)]
