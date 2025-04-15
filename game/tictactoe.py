class TicTacToe:
    def __init__(self):
        # Initialize empty board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
        # Display the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    def print_board_nums(self):
        # Display the position numbers for reference
        number_board = [[str(i+j*3) for i in range(1, 4)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        # Returns list of available positions (0-8)
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        # Checks if there are empty squares
        return ' ' in self.board
    
    def num_empty_squares(self):
        # Returns the number of empty squares
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # Make a move if valid
        if self.board[square] == ' ':
            self.board[square] = letter
            
            # Check for win
            if self.find_winner(square, letter):
                self.current_winner = letter
                
            return True
        return False
    
    def find_winner(self, square, letter):
        # Check if the most recent move won the game
        
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
            
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
            
        # Check diagonals
        # Only check diagonals if the square is on a diagonal
        if square % 2 == 0:
            # Top-left to bottom-right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
                
            # Top-right to bottom-left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
                
        return False