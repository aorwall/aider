class SgfTree:
    def __init__(self, properties: Dict[str, List[str]] = None, children: List['SgfTree'] = None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other

def parse_sgf_string(sgf_string: str) -> SgfTree:
    if not sgf_string.startswith("(;"):
        raise ValueError("tree missing")

    properties, *children = re.split(r"\(;([^()]*)\)", sgf_string)

    if not properties:
        raise ValueError("tree with no nodes")

    root_properties = _parse_node_properties(properties)

    if not children:
        return SgfTree(root_properties)

    children_trees = [_parse_sgf_string(child) for child in children]

    return SgfTree(root_properties, children_trees)

def _parse_sgf_string(sgf_string: str) -> SgfTree:
    if not sgf_string.startswith("("):
        raise ValueError("properties without delimiter")

    properties, *children = re.split(r"\((\s*[A-Z]+\s*[^\s\)]*\s*)", sgf_string)

    if not properties:
        raise ValueError("properties without delimiter")

    root_properties = _parse_node_properties(properties)

    if not children:
        return SgfTree(root_properties)

    children_trees = [_parse_sgf_string(child) for child in children]

    return SgfTree(root_properties, children_trees)

def _parse_node_properties(properties: str) -> Dict[str, List[str]]:
    if not properties.startswith(";"):
        raise ValueError("properties without delimiter")

    properties = properties[1:]
    parsed_properties = {}

    for prop in properties.split(";"):
        key, *values = prop.strip().split(" ")
        if not key.isupper():
            raise ValueError("property must be in uppercase")

        parsed_properties[key] = values

    return parsed_properties

def main():
    sgf_string = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"
    tree = parse_sgf_string(sgf_string)
    print(tree)

if __name__ == "__main__":
    main()
