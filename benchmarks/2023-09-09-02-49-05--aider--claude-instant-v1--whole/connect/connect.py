class ConnectGame:
    def __init__(self, board):
        self.board = board

    def get_winner(self):
        board = self.board
        rows = len(board) 
        cols = len(board[0])

        # Check for horizontal connection
        for r in range(rows):
            piece = board[r][0]
            if piece != '.':
                connected = True
                for c in range(cols):
                    if board[r][c] != piece:
                        connected = False
                        break
                if connected:
                    return piece

        # Check for vertical connection
        for c in range(cols):
            piece = board[0][c] 
            if piece != '.':
                connected = True
                for r in range(rows):
                    if board[r][c] != piece:
                        connected = False
                        break
                if connected: 
                    return piece

        # Check for diagonal connections
        for r in range(rows-1):
            for c in range(cols-1):
                piece = board[r][c]
                if piece != '.':
                    if (board[r][c] == board[r+1][c+1] or 
                        board[r][c] == board[r+1][c-1]):
                        return piece

        # No winner found
        return ""
