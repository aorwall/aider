def from_pov(self, from_node):
    if self.label == from_node:
        return self

    for child in self.children:
        result = child.from_pov(from_node)
        if result is not None:
            result.children.append(self)
            return result

    return None
