import re

def parse(markdown):
    """
    Refactored the Markdown parser to be more readable and maintainable.
    - Extracted regex patterns to constants at the top for readability
    - Split parsing into separate functions for each element (headings, lists, etc)  
    - Added comments to explain the logic
    - Removed unnecessary variables
    - Standardized formatting (spacing, etc)
    """

    HEADING_PATTERN = r'(#{1,6}) (.*)'
    LIST_ITEM_PATTERN = r'\* (.*)'

    html = parse_headings(markdown)
    html = parse_lists(html) 
    html = parse_paragraphs(html)
    html = parse_emphasis(html)

    return html


def parse_headings(markdown):
    """Parse heading levels with regex and return HTML"""

    lines = markdown.split('\n')
    html = ''

    for line in lines:
        match = re.match(HEADING_PATTERN, line)
        if match:
            level = len(match.group(1))
            html += f'<h{level}>{match.group(2)}</h{level}>\n'
        else:
            html += line + '\n'

    return html


def parse_lists(markdown):
    """Parse bullet list items with regex and return HTML"""

    lines = markdown.split('\n')
    html = ''
    in_list = False

    for line in lines:

        match = re.match(LIST_ITEM_PATTERN, line)
        if match:

            if not in_list:
                html += '<ul>\n'
                in_list = True

            html += f'<li>{match.group(1)}</li>\n'

        elif in_list:
            html += '</ul>\n'
            in_list = False

        else:
            html += line + '\n'

    if in_list:
        html += '</ul>'

    return html


def parse_paragraphs(markdown):
    """Wrap lines in <p> if they are not other elements"""

    lines = markdown.split('\n')
    html = ''

    for line in lines:
        if not re.match(r'<h|<ul|<li|<p', line):
            html += f'<p>{line}</p>\n'
        else:
            html += line + '\n'

    return html
