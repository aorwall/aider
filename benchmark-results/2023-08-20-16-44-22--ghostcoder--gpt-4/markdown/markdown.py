import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        header = parse_header(i)
        if header:
            i = header
        else:
            i, in_list, in_list_append = parse_list_item(i, in_list, in_list_append)
            i = parse_paragraph(i)
            i = parse_bold(i)
            i = parse_italic(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

def parse_header(line):
    match = re.match("(#{1,6}) (.*)", line)
    if match:
        num = len(match.group(1))
        return f"<h{num}>{match.group(2)}</h{num}>"
    return None

def parse_list_item(line, in_list, in_list_append):
    match = re.match(r'\* (.*)', line)
    if match:
        curr = match.group(1)
        curr = parse_bold(curr)
        curr = parse_italic(curr)
        if not in_list:
            in_list = True
            return f'<ul><li>{curr}</li>', in_list, False
        else:
            return f'<li>{curr}</li>', in_list, False
    else:
        if in_list:
            in_list_append = True
            in_list = False
        return line, in_list, in_list_append

def parse_paragraph(line):
    if not re.match('<h|<ul|<p|<li', line):
        return f'<p>{line}</p>'
    return line

def parse_bold(line):
    match = re.match('(.*)__(.*)__(.*)', line)
    if match:
        return f"{match.group(1)}<strong>{match.group(2)}</strong>{match.group(3)}"
    return line

def parse_italic(line):
    match = re.match('(.*)_(.*)_(.*)', line)
    if match:
        return f"{match.group(1)}<em>{match.group(2)}</em>{match.group(3)}"
    return line