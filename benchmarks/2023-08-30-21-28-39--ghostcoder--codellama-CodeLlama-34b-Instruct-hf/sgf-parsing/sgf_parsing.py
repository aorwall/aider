def parse(input_string):
    # Create an empty SgfTree object
    tree = SgfTree()

    # Split the input string into lines
    lines = input_string.splitlines()

    # Iterate over the lines and parse the properties and children
    for line in lines:
        # Split the line into key-value pairs
        key, value = line.split("[", 1)
        key = key.strip()
        value = value.strip()

        # Add the property to the tree
        tree.properties[key] = value

        # Check if the line has children
        if "(" in value:
            # Split the value into children
            children = value.split("(")

            # Add the children to the tree
            for child in children:
                tree.children.append(SgfTree(properties={child.strip(): None}))

    return tree