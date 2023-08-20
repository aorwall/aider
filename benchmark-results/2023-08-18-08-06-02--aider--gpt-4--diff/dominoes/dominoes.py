def can_chain(dominoes):
    if not dominoes:
        return []
    used = [False] * len(dominoes)
    chain = []

    def dfs(last):
        if len(chain) == len(dominoes):
            return last == chain[0][0]
        for i in range(len(dominoes)):
            if used[i]:
                continue
            a, b = dominoes[i]
            if a == last:
                used[i] = True
                chain.append(dominoes[i])
                if dfs(b):
                    return True
                chain.pop()
                used[i] = False
            elif b == last:
                used[i] = True
                chain.append((b, a))
                if dfs(a):
                    return True
                chain.pop()
                used[i] = False
        return False

    for i in range(len(dominoes)):
        used[i] = True
        chain.append(dominoes[i])
        if dfs(dominoes[i][1]):
            return chain
        chain.pop()
        used[i] = False
    return []
