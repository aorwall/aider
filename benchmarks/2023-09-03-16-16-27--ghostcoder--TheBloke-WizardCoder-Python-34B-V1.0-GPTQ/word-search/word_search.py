class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    RIGHT = 'r'
    LEFT = 'l'
    DOWN = 'd'
    UP = 'u'
    DIAGONAL_DOWN_RIGHT = 'dr'
    DIAGONAL_DOWN_LEFT = 'dl'
    DIAGONAL_UP_RIGHT = 'ur'
    DIAGONAL_UP_LEFT = 'ul'

    def __init__(self, puzzle):
        self._puzzle = [list(row) for row in puzzle] # convert string into list of lists
        self._rows = len(self._puzzle)
        self._cols = len(self._puzzle[0])


    def _traverse_horizontally(self, word, direction, point):
        """Traverses the matrix horizontally to see if the word exists"""
        start = end = point
        for i in range(len(word)):
            if point.x < 0 or point.x >= self._cols or point.y < 0 or point.y >= self._rows or self._puzzle[point.y][point.x] != word[i]:
                return False, None, None
            elif direction == self.RIGHT:
                point.x += 1
            else:
                point.x -= 1
        end.x = point.x - 1 if direction == self.LEFT else point.x
        return True, start, end

    def _traverse_vertically(self, word, direction, point):
        """Traverses the matrix vertically to see if the word exists"""
        start = end = point
        for i in range(len(word)):
            if point.x < 0 or point.x >= self._cols or point.y < 0 or point.y >= self._rows or self._puzzle[point.y][point.x] != word[i]:
                return False, None, None
            elif direction == self.DOWN:
                point.y += 1
            else:
                point.y -= 1
        end.y = point.y - 1 if direction == self.UP else point.y
        return True, start, end

    def _traverse_diagonals(self, word, direction, point):
        """Traverses the matrix diagonally to see if the word exists"""
        start = end = point
        for i in range(len(word)):
            if point.x < 0 or point.x >= self._cols or point.y < 0 or point.y >= self._rows or self._puzzle[point.y][point.x] != word[i]:
                return False, None, None
            elif direction == self.DIAGONAL_DOWN_RIGHT:
                point.x += 1
                point.y += 1
            elif direction == self.DIAGONAL_DOWN_LEFT:
                point.x -= 1
                point.y += 1
            elif direction == self.DIAGONAL_UP_RIGHT:
                point.x += 1
                point.y -= 1
            else:
                point.x -= 1
                point.y -= 1
        end.x = point.x - 1 if direction == self.DIAGONAL_DOWN_LEFT else point.x
        end.y = point.y - 1 if direction == self.DIAGONAL_UP_LEFT else point.y
        return True, start, end

    def search(self, word):
        """Returns the start and end points of the word if it exists in the matrix"""
        for i in range(self._rows):
            for j in range(self._cols):
                for direction in [self.RIGHT, self.LEFT, self.DOWN, self.UP, self.DIAGONAL_DOWN_RIGHT, self.DIAGONAL_DOWN_LEFT, self.DIAGONAL_UP_RIGHT, self.DIAGONAL_UP_LEFT]:
                    if direction in {self.RIGHT, self.LEFT}:
                        status, start, end = self._traverse_horizontally(word, direction, Point(j, i))
                    elif direction in {self.DOWN, self.UP}:
                        status, start, end = self._traverse_vertically(word, direction, Point(j, i))
                    else:
                        status, start, end = self._traverse_diagonals(word, direction, Point(j, i))
                    if status:
                        return start, end
        return None
