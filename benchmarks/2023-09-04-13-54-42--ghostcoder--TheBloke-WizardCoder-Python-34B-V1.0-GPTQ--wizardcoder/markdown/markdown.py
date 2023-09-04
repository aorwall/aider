import re
from typing import List

class MarkdownParser:
    def __init__(self):
        self._lines = []

    def add_line(self, line: str) -> None:
        self._lines.append(line)

    def parse(self) -> str:
        result = ""
        in_list = False
        in_list_append = False

        for i, line in enumerate(self._lines):
            # Check if it's a header
            match = re.match("^#{1,6} (.*)", line)
            if match:
                heading_level = len(match.groups()[0])
                line = f"<h{heading_level}>{match.groups()[0]}</h{heading_level}>"

            # Check if it's an unordered list item
            match = re.match("^ *[-+\*] (.*)", line)
            if match:
                if not in_list:
                    in_list = True
                    line = f"<ul>\n<li>{match.groups()[0].strip()} </li>"
                else:
                    line = f"\n<li>{match.groups()[0].strip()} </li>"

            # Check if it's an ordered list item
            match = re.match("^ *\d*\. (.*)", line)
            if match:
                if not in_list:
                    in_list = True
                    line = f"<ol>\n<li>{match.groups()[0].strip()} </li>"
                else:
                    line = f"\n<li>{match.groups()[0].strip()} </li>"

            # Check if it's a paragraph
            match = re.match("<h|<ul|<ol|<li", line)
            if not match:
                line = f"<p>{line}</p>"

            # Check if it's strong text
            while "__" in line:
                match = re.search("^(.*?)__(.*?)__(.*)$", line)
                if match:
                    line = match.group(1) + "<strong>" + match.group(2) + "</strong>" + match.group(3)
                else:
                    break

            # Check if it's italic text
            while "_" in line:
                match = re.search("^(.*?)_(.*?)_(.*)$", line)
                if match:
                    line = match.group(1) + "<em>" + match.group(2) + "</em>" + match.group(3)
                else:
                    break

            # Append the processed line to the result
            result += line

            # If we were previously in a list but this line doesn't continue it, close the list tag
            if in_list and not re.match("^ *(-|\+|\*|\d+\.) ", line):
                in_list = False
                result += "\n</ul>" if in_list_append else "\n</ol></li>"
                in_list_append = False

        # Close any remaining lists
        if in_list:
            result += "\n</ul>" if not in_list_append else "\n</ol></li>"

        return result

if __name__ == "__main__":
    parser = MarkdownParser()
    parser.add_line("# Heading")
    parser.add_line("- Item 1")
    parser.add_line("- Item 2")
    print(parser.parse())


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('##### (.*)', i) is not None:
            i = '<h5>' + i[6:] + '</h5>'
        elif re.match('#### (.*)', i) is not None:
            i = '<h4>' + i[5:] + '</h4>'
        elif re.match('### (.*)', i) is not None:
            i = '<h3>' + i[4:] + '</h3>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
