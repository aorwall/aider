import re


def parse(markdown):
    lines = markdown.split('\n')
    parsed_lines = []
    list_stack = []

    for line in lines:
        if re.match(r'###### (.*)', line):
            parsed_lines.append(f'<h6>{line[7:]}</h6>')
        elif re.match(r'##### (.*)', line):
            parsed_lines.append(f'<h5>{line[6:]}</h5>')
        elif re.match(r'#### (.*)', line):
            parsed_lines.append(f'<h4>{line[5:]}</h4>')
        elif re.match(r'### (.*)', line):
            parsed_lines.append(f'<h3>{line[4:]}</h3>')
        elif re.match(r'## (.*)', line):
            parsed_lines.append(f'<h2>{line[3:]}</h2>')
        elif re.match(r'# (.*)', line):
            parsed_lines.append(f'<h1>{line[2:]}</h1>')
        elif re.match(r'\* (.*)', line):
            item = re.match(r'\* (.*)', line).group(1)
            if not list_stack:
                parsed_lines.append('<ul>')
            list_stack.append(item)
            parsed_lines.append(f'<li>{parse_inline_markup(item)}</li>')
        else:
            if list_stack:
                parsed_lines.append('</ul>')
                list_stack.clear()
            parsed_lines.append(f'<p>{parse_inline_markup(line)}</p>')

    if list_stack:
        parsed_lines.append('</ul>')

    return ''.join(parsed_lines)


def parse_inline_markup(line):
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    return line
