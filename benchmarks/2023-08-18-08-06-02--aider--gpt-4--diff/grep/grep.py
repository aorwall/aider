import re

def grep(pattern, flags, files):
    result = []
    for file in files:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                line = line.rstrip('\n')
                if '-i' in flags:
                    line_to_match = line.lower()
                    pattern = pattern.lower()
                else:
                    line_to_match = line
                if '-x' in flags and line_to_match != pattern:
                    continue
                if '-v' in flags and re.search(pattern, line_to_match):
                    continue
                if '-l' in flags:
                    result.append(file)
                    break
                if '-n' in flags:
                    line = f"{file}:{i}:{line}"
                elif len(files) > 1:
                    line = f"{file}:{line}"
                if re.search(pattern, line_to_match):
                    result.append(line)
    return '\n'.join(result)
