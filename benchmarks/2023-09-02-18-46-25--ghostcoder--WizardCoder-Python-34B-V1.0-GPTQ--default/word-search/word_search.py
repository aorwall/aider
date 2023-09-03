class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = [list(row) for row in puzzle]  # convert rows into lists of characters
        self.rows = len(self.puzzle)
        if self.rows > 0:
            self.cols = len(self.puzzle[0])
        else:
            self.cols = 0

    def search(self, word):
        result = []
        # horizontal search
        for i in range(self.rows):
            row = ''.join(self.puzzle[i]).find(word)
            while row != -1:
                start = Point()
                end = Point()
                start.x = i
                start.y = row
                end.x = i
                end.y = row + len(word) - 1
                result.append((start, end))
                row = ''.join(self.puzzle[i][row+len(word):].find(word))   # added missing parenthesis here

        # vertical search
        for j in range(self.cols):
            col = ''
            for i in range(self.rows):
                col += self.puzzle[i][j]
            row = col.find(word)
            while row != -1:
                start = Point()
                end = Point()
                start.x = row
                start.y = j
                end.x = row + len(word) - 1
                end.y = j
                result.append((start, end))

        # diagonal downwards search
        for i in range(self.rows-len(word)+1):
            for j in range(self.cols-len(word)+1):
                if all([self.puzzle[i+k][j+k] == word[k] for k in range(len(word)]):
                    start = Point()
                    end = Point()
                    start.x = i
                    start.y = j
                    end.x = i + len(word) - 1
                    end.y = j + len(word) - 1
                    result.append((start, end))
                elif all([self.puzzle[i+k][self.cols-1-j-k] == word[k] for k in range(len(word)]):
                    start = Point()
                    end = Point()
                    start.x = i
                    start.y = self.cols-1-j
                    end.x = i + len(word) - 1
                    end.y = self.cols-1-(j+len(word)-1)
                    result.append((start, end))
        return result