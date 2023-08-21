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
            i, in_list, in_list_append = parse_list(i, in_list, in_list_append)
            i = parse_text(i, in_list)
        res += i
    if in_list:
        res += '</ul>'
    return res

def parse_header(line):
    match = re.match('(#{1,6}) (.*)', line)
    if match:
        num = len(match.group(1))
        return '<h{0}>{1}</h{0}>'.format(num, match.group(2))
    return None

def parse_list(line, in_list, in_list_append):
    match = re.match(r'\* (.*)', line)
    if match:
        curr = parse_text(match.group(1), True)
        if not in_list:
            in_list = True
            line = '<ul><li>' + curr + '</li>'
        else:
            line = '<li>' + curr + '</li>'
    else:
        if in_list:
            in_list_append = True
            in_list = False
    if in_list_append:
        line = '</ul>' + line
        in_list_append = False
    return line, in_list, in_list_append

def parse_text(line, in_list=False):
    line = re.sub('__(.*)__', r'<strong>\1</strong>', line)
    line = re.sub('_(.*)_', r'<em>\1</em>', line)
    if not re.match('<h|<ul|<p|<li', line) and not in_list:
        line = '<p>' + line + '</p>'
    return line
