import re

def grep(pattern, flags, files):
    results = []
    flags = set(flags)
    for file in files:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                if '-i' in flags:
                    match = re.search(pattern, line, re.IGNORECASE)
                else:
                    match = re.search(pattern, line)
                if '-x' in flags and match:
                    match = match.group() == line.rstrip('\n')
                if '-v' in flags:
                    match = not match
                if match:
                    if '-l' in flags:
                        results.append(file)
                        break
                    result = ''
                    if len(files) > 1:
                        result += f'{file}:'
                    if '-n' in flags:
                        result += f'{i}:'
                    result += line.rstrip('\n')
                    results.append(result)
    return '\n'.join(results)
