import re
from typing import List

def count_rectangles(string: str) -> int:
    pattern = r"(?:\+-+)+\+" # Matches top border of a rectangle
    matches = list(re.finditer(pattern, string))
    if not matches:
        return 0

    max_match = max(matches, key=lambda m: m.end())
    start_index = max_match.start()
    end_index = max_match.end() - 1

    while end_index < len(string) and string[end_index].isalpha():
        end_index += 1

    lines = [line.strip() for line in string[start_index:end_index].split("\n")]
    height = len(lines)
    width = max([len(line) for line in lines])

    num_horizontal_borders = sum(1 for c in string[:start_index] if c == "+")
    num_vertical_borders = sum(1 for line in lines if line[0] == "|" and line[-1] == "|")

    total_area = num_horizontal_borders * num_vertical_borders
    single_rectangle_area = height * width

    return total_area // single_rectangle_area

def rectangles(strings: List[str]) -> int:
    return sum(count_rectangles(string) for string in strings)