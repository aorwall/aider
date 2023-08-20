import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        html = parse_line(line)
        if html is None:
            if in_list:
                in_list_append = True
                in_list = False
            html = parse_paragraph(line)
        elif html.startswith('<ul'):
            if not in_list:
                in_list = True
            else:
                html = html[4:]
        elif in_list:
            in_list_append = True
            in_list = False
        if in_list_append:
            html = '</ul>' + html
            in_list_append = False
        res += html
    if in_list:
        res += '</ul>'
    return res

def parse_line(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i) and not line.startswith('#' * (i + 1)):
            return '<h{0}>{1}</h{0}>'.format(i, line[i+1:])
    if line.startswith('* '):
        content = parse_emphasis(line[2:])
        return '<ul><li>{0}</li>'.format(content)
    return None

def parse_paragraph(line):
    return '<p>{0}</p>'.format(parse_emphasis(line))

def parse_emphasis(line):
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    return line
