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
    
    def __init__(self, players, board_size):
        self.board = []
        self.size = board_size
        self.current_player = players[0]
        self.players = players
    
    def init_board(self):
        board = []

        for row in xrange(self.size):
            board.append([])

        for sub_list in board:
            for x in xrange(self.size):
                sub_list.append(" ")

        self.board = board

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
            return True
        else:
            print "invalid move, try again."
            return False
    
    def move_valid(self, x, y):
        # check if row (x) & column (y) are within matrix
        if x >= self.size or y >= self.size:
            return False
        
        # check if row & col are empty
        if self.board[x][y] != " ":
            return False
        return True
    
    def gameover(self, x, y, player):
        # Check if there is a winner
        # check if given row has a win
        row = self.board[x]
        winner_row = True

        # go through each cell in the row & check if that cell equals current symbol
        for cell in row:
            # if one of those cells doesn't equal the current player - no win on row
            if cell != player:
                winner_row = False
                break
        # if we got through the loop and winner_row is still true, we are a winner
        if winner_row:
            print "Player %s is the winner!" % player
            return True

        # check if given col has a win
        winner_col = True

        for row in self.board:
            if row[y] != player:
                winner_col = False
                break
        
        if winner_col:
            print "Player %s is the winner!" % player
            return True            
       
        # check if diag has a win
        winner_diag1 = True
        current1 = 0
        
        # check each row, but are only checking a specific cell in that row
        while current1 < self.size:
            if self.board[current1][current1] != player:
                winner_diag1 = False
                break
            current1 += 1

        if winner_diag1:
            print "Player %s is the winner!" % player
            return True
        
        winner_diag2 = True
        current2 = 0
        
        # similar to above but different cell check
        while current2 < self.size:
            cell = (self.size-1) - current2
            if self.board[current2][cell] != player:
                winner_diag2 = False
                break
            current2 += 1

        if winner_diag2:
            print "Player %s is the winner!" % player
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
# TODO: make the board 3D
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
    # need to have even sized board (height & width same)
    board_size = int(raw_input("How many rows in the game board (column # will the be same as you enter here)? > "))
    
    while board_size < 3:
        board_size = int(raw_input("Please enter a number larger than 2 to make this a fair game > "))
    
    game_board = Board([player1, player2], board_size)
    game_board.init_board()
    
    while True:
        current_player = game_board.current_player.symbol
        print "current player: ", current_player
        game_board.print_board()
        coords = raw_input("Where would you like to play? (row column) - remember, zero-indexed! ")
        coord_list = coords.split(" ")
        row = int(coord_list[0])
        col = int(coord_list[1]) 
        if game_board.make_move(row, col):
            game_board.switch_player()
            if game_board.gameover(row, col, current_player):
                break

    game_board.print_board()

if __name__ == '__main__':
    
    main()