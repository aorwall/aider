import re

def parse(text):
    return re.sub(r'#(.*)', r'<h1>\1</h1>', text)

class MarkdownParser:
    def parse(self, text):
        return parse(text)
