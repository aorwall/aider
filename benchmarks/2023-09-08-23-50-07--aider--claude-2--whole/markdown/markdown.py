import re

def parse(markdown):

    # Split input into lines
    lines = markdown.split('\n')

    # Output HTML
    html = ''

    # Track state
    in_list = False
    in_list_append = False

    for line in lines:
        
        # Headings
        if re.match(r'#{1,6} (.*)', line):
            level = len(re.match(r'#*', line).group(0))
            html += '<h{0}>{1}</h{0}>'.format(level, re.sub(r'#+ ?', '', line))

        # Lists
        elif re.match(r'\* (.*)', line):
            if not in_list:
                html += '<ul>' 
                in_list = True
            html += '<li>' + re.sub(r'\* ', '', line) + '</li>'
        else:
            if in_list:
                html += '</ul>'
                in_list = False
                in_list_append = True
        
        # Paragraphs
        if not re.match(r'<h|<ul|<p|<li', line):
            html += '<p>' + line + '</p>'
            
        # Bold
        bold = re.compile(r'__(.*)__')
        line = bold.sub(r'<strong>\1</strong>', line)
        
        # Italics
        italics = re.compile(r'_(.*)_')
        line = italics.sub(r'<em>\1</em>', line)
        
        # Append list close tag
        if in_list_append:
            html += '</ul>'
            in_list_append = False
            
        # Add processed line
        html += line

    # Close any open lists
    if in_list:
        html += '</ul>'

    return html
