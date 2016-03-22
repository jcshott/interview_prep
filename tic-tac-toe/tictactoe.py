#
# Design and Build a Tic-Tac-Toe Game
#
# Board, 2 Players
#
# 1. Select player 1 (by default O)
# 2. Player makes move (action):
#    -> evaluate if action is valid (check if space is empty)
#    -> make move
# 3. Check if anyone (player who moved) has won
# 4. Switch Player (return to Step 1)
#

class Board(object):
    
    def __init__(self, players):
        self.board = [[" ", " ", " "], 
                      [" ", " ", " "], 
                      [" ", " ", " "]]
        self.current_player = players[0]
        self.players = players
        
    def print_board(self):
        """ Prints current board state """
        
        for row in self.board:
            print "|",
            for column in row:
                print column, # remove newline
                print "|",
            print
            
    def make_move(self, x, y):
        symbol = self.current_player.symbol
        if self.move_valid(x, y):
            self.board[x][y] = symbol
        else:
            print "invalid move, try again."
    
    def move_valid(self, x, y):
        # check if row & column are within matrix
        if x > 2 or y > 2:
            return False
        
        # check if row & col are empty
        if self.board[x][y] != " ":
            return False
        return True
    
    def gameover(self, x, y):
        # Check if there is a winner
        # check if given row has a win
        row = self.board[x]
        if row[0] == row[1] and row[1] == row[2]:
            print "Winner"
            return True
        # check if given col has a win
        if (self.board[0][y] == self.board[1][y] and 
            self.board[1][y] == self.board[2][y]):
            print "Winner"
            return True
        # check if diag has a win
        if (self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2]) and self.board[0][0] != " ":
            print "Winner"
            return True
        if (self.board[0][2] == self.board[1][1] and 
            self.board[1][1] == self.board[2][0]) and self.board[0][2] != " ":
            print "Winner"
            return True
        # check if everything has been filled (draw)
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        print "Draw"
        return True
        
    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

class Player(object):
    
    def __init__(self, symbol):
        self.symbol = symbol

        
def main():
#
#
# Board, 2 Players
#
# 1. Select player 1 (by default O)
# 2. Player makes move (action):
#    -> evaluate if action is valid (check if space is empty)
#    -> make move
# 3. Check if anyone (player who moved) has won
# 4. Switch Player (return to Step 1)
#
    """ Start the game """
    player1 = Player("O")
    player2 = Player("X")
    game_board = Board([player1, player2])
    
    while True:
        print "current player: ", game_board.current_player.symbol
        game_board.print_board()
        coords = raw_input("Where would you like to play? (row column) ")
        coord_list = coords.split(" ")
        row = int(coord_list[0])
        col = int(coord_list[1])
        game_board.make_move(row, col)
        if game_board.gameover(row, col):
            break
        game_board.switch_player()
    game_board.print_board()

main()