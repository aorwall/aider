import re

def grep(pattern, flags, files):

    flags_dict = parse_flags(flags)

    matching_lines = ""

    for filename in files:

        with open(filename) as f:
            file_lines = f.readlines()

        for line_num, line in enumerate(file_lines):

            if matches(pattern, line, flags_dict):
                if flags_dict['-l']:
                    matching_lines += filename + "\n"
                else:
                    if flags_dict['-n']:
                        matching_lines += f"{filename}:{line_num+1}:{line}"
                    else:
                        matching_lines += f"{filename}:{line}" if filename else line
                        
        matching_lines += "\n"

    return matching_lines

def parse_flags(flags):
   # same as before

def matches(pattern, line, flags_dict):
   # same as before 
