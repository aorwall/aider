import re
from collections import deque

class SgfTree:
    ...

def parse(input_string):
    input_string = input_string.replace('\t', '')       # remove tabs which may cause issues
    input_string = input_string.replace('\n', '\\n')   # escape newlines
    input_string = input_string.replace(']', ']\n')    # each property ends with a newline
    input_string = re.sub(r'(?<!\\)\\\[', '], [', input_string) # each node ends with ], [
    input_string = re.sub(r'(?<!\\)\\\)', '], ', input_string) # each tree ends with ], 
    input_string = re.sub(r'(?<!\\)\\\(', '](', input_string) # each variation ends with ](
    input_string = re.sub(r'(?<!\\)\\\]', '])', input_string) # end of file should be ]
    input_string += '\n'                               # ensure well formed
    stream = deque(re.findall(r'\w|\W', input_string))
    return SgfTree._parse_tree(stream)
