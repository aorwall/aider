
class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
        self.player_o = 'O'
        self.player_x = 'X'
        self.winner = None

    def get_winner(self):
        # Check if there is a winner
        if self.winner:
            return self.winner

        # Check if the game is over
        if self.is_game_over():
            return None

        # Check if player O has won
        if self.has_won(self.player_o):
            self.winner = self.player_o
            return self.winner

        # Check if player X has won
        if self.has_won(self.player_x):
            self.winner = self.player_x
            return self.winner

        # If the game is not over and no winner has been found, return None
        return None

    def is_game_over(self):
        # Check if the game is over by checking if all fields are filled
        for row in self.board:
            for field in row:
                if field == '.':
                    return False
        return True

    def has_won(self, player):
        # Check if the player has won by checking if they have connected all their pieces
        for row in self.board:
            for field in row:
                if field == player:
                    # Check if the player has connected all their pieces in a row
                    if self.is_connected(player, row):
                        return True

                    # Check if the player has connected all their pieces in a column
                    if self.is_connected(player, [field for field in row]):
                        return True

        return False

    def is_connected(self, player, sequence):
        # Check if the player has connected all their pieces in a sequence
        for i in range(len(sequence) - 1):
            if sequence[i] == player and sequence[i + 1] == player:
                return True
        return False
