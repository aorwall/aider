class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.height = len(puzzle)
        self.width = len(puzzle[0])

    def search(self, word):
        for y in range(self.height):
            for x in range(self.width):
                if self._search_from(word, x, y):
                    return True
        return False
    
    def _search_from(self, word, x, y):
        # Check each direction
        for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
            # See if we can find the word starting at x, y
            first = Point(x, y)
            last = self._find_end(word, x, y, dx, dy)
            if last:
                return first, last
        return None
    
    def _find_end(self, word, x, y, dx, dy):
        # Follow direction dx, dy to find end letter
        last_letter = len(word) - 1
        for i in range(len(word)):
            if x >= self.width or y >= self.height:
                return None
            
            letter = self.puzzle[y][x]
            if letter != word[i]:
                # Letter didn't match, word not found
                return None
            if i == last_letter:
                # Found the last letter, return it
                return Point(x, y)
            
            # Move to next letter
            x += dx
            y += dy
        
        # Fell off the puzzle before finding the last letter
        return None
