import re
from typing import Union

def parse_octal(input_string: str) -> Union[int, None]:
    """Converts a given octal string into its decimal representation."""

    def _valid_octal(octal_str: str) -> bool:
        pattern = r"^[0-7]+$"
        return bool(re.match(pattern, octal_str))

    if not isinstance(input_string, str) or not _valid_octal(input_string):
        return None

    decimal = 0
    for index, value in enumerate(reversed(input_string)):
        decimal += int(value) * (8 ** index)

    return decimal