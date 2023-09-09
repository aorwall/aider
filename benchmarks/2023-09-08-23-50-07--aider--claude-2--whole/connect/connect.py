
class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def get_winner(self):
        # Check for O winner going top to bottom
        for y in range(self.height):
            o_connected = True
            for x in range(self.width):
                if self.board[y][x] != 'O':
                    o_connected = False
                    break
            if o_connected:
                return 'O'
        
        # Check for X winner going left to right
        for x in range(self.width):
            x_connected = True
            for y in range(self.height):
                if self.board[y][x] != 'X':
                    x_connected = False
                    break
            if x_connected:
                return 'X'

        # Check for O winner going left to right
        for x in range(self.width):
            o_connected = True
            for y in range(self.height):
                if self.board[y][x] != 'O':
                    o_connected = False
                    break
            if o_connected:
                return 'O'

        # Check for X winner going top to bottom
        for y in range(self.height):
            x_connected = True
            for x in range(self.width):
                if self.board[y][x] != 'X':
                    x_connected = False
                    break
            if x_connected:
                return 'X'
        
        # No winner
        return None
