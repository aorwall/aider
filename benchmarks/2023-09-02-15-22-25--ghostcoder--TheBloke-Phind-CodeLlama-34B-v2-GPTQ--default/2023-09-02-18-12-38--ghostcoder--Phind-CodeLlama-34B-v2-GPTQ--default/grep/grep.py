import os
import re
def grep(pattern, flags, files):
    result = []

    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            lines = f.readlines()

        for lineno, line in enumerate(lines):
            if '-n' in flags:
                prefix = '{}:'.format(os.path.basename(file))
                line_number = str(lineno + 1)
                line = '{}{}:{}'.format(prefix, line_number, line)

            match = bool(re.search(pattern, line, re.IGNORECASE if '-i' in flags else 0))

            if ('-v' not in flags and not match) \
                    or (match and '-x' in flags and line != pattern):
                continue

            if '-l' in flags:
                if file not in result:
                    result.append(file)
            elif '-o' in flags:
                matches = re.findall(pattern, line)
                result.extend(['{}:{}'.format(os.path.basename(file), m) for m in matches])
            else:
                result.append(line.strip())

    return '\n'.join(result)
