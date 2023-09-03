import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''

    # State variables
    in_list = False
    in_list_append = False
    for i in lines:
        header_match = re.match('(#{1,6}) (.*)', i)

        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)

            i = f'<h{level}>{text}</h{level}>'
        elif re.match('\\* (.*)', i):
            list_item_match = re.match('\\* (.*)', i)
            curr = list_item_match.group(1)

            strong_match = re.match('(.*)__(.*)__(.*)', curr)
            em_match = re.match('(.*)_(.*)_(.*)', curr)

            if strong_match:
                curr = strong_match.group(1) + '<strong>' + \
                       strong_match.group(2) + '</strong>' + strong_match.group(3)
            if em_match:
                curr = em_match.group(1) + '<em>' + em_match.group(2) + \
                       '</em>' + em_match.group(3)

            if not in_list:
                in_list = True
                i = '<ul><li>' + curr + '</li>'
            else:
                in_list_append = True
                i = '<li>' + curr + '</li>'
        else:
            i = '<p>' + i + '</p>'

        strong_match = re.match('(.*)__(.*)__(.*)', i)
        if strong_match:
            i = strong_match.group(1) + '<strong>' + \
               strong_match.group(2) + '</strong>' + strong_match.group(3)

        em_match = re.match('(.*)_(.*)_(.*)', i)
        if em_match:
            i = em_match.group(1) + '<em>' + em_match.group(2) + \
               '</em>' + em_match.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False

        res += i

    # Close the list if necessary
    if in_list:
        res += '</ul>'
    return res
