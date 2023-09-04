import os
import re

def grep(pattern, flags, files):
    results = []

    for fname in files:
        with open(fname) as f:
            for lineno, line in enumerate(f):
                line = line.rstrip()

                # Check if the line matches the pattern
                if re.search(pattern, line, re.IGNORECASE if 'i' in flags else 0):
                    if 'v' in flags:
                        continue

                    if 'n' in flags:
                        line = '{}:{}'.format(lineno+1, line)

                    results.append('{}:{}'.format(fname, line))

                elif 'v' in flags and not re.match(pattern, line, re.IGNORECASE if 'i' in flags else 0):
                    if 'n' in flags:
                        line = '{}:{}'.format(lineno+1, line)

                    results.append('{}:{}'.format(fname, line))

    if len(results) > 0 and 'l' in flags:
        return [os.path.basename(result.split(':')[0]) for result in results]

    return '\n'.join(results)   ## Join all elements in the list into a single string
