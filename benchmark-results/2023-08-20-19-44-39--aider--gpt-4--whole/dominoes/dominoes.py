def can_chain(dominoes):
    if not dominoes:
        return []

    # Create a graph
    graph = {i: [] for i in range(7)}
    degrees = [0] * 7
    for a, b in dominoes:
        graph[a].append(b)
        graph[b].append(a)
        degrees[a] += 1
        degrees[b] += 1

    # Find the starting node
    start = next((i for i, v in enumerate(degrees) if v % 2 == 1), 0)

    # Perform DFS
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if len(path) == len(dominoes) + 1:
            return [(path[i-1], path[i]) for i in range(1, len(path))]
        for neighbor in graph[node]:
            if neighbor not in path or (node, neighbor) in dominoes:
                stack.append((neighbor, path + [neighbor]))
                if (node, neighbor) in dominoes:
                    dominoes.remove((node, neighbor))
                else:
                    dominoes.remove((neighbor, node))
    return []
