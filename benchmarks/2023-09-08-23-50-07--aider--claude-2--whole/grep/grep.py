import re

def grep(pattern, flags, files):

    regex_flags = 0
    if '-i' in flags:
        regex_flags |= re.IGNORECASE

    match_entire_line = '-x' in flags
    invert_match = '-v' in flags
    show_line_numbers = '-n' in flags
    show_file_names = '-l' not in flags

    matches = []
    for filename in files:
        with open(filename, 'r') as f:
            line_num = 0
            for line in f:
                line_num += 1
                if match_entire_line:
                    is_match = line.strip() == pattern
                else:
                    is_match = re.search(pattern, line, regex_flags) is not None
                if is_match and not invert_match or not is_match and invert_match:
                    if show_line_numbers:
                        line = f'{filename}:{line_num}: {line}'
                    elif show_file_names:
                        line = f'{filename}: {line}'
                    matches.append(line)

    if show_file_names:
        return set(matches)
    return '\n'.join(matches)
