import time
from game.utilities import clear_screen, handle_quit
from game.user_interface import print_title, Colors
from players.players import HumanPlayer

class TicTacToe:
    def __init__(self):
        # Initialize empty board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
        # Display the board with colors
        print(f"{Colors.BOLD}Current Board:{Colors.RESET}")
        
        for i in range(3):
            # Print row with colored X and O
            print(f"{Colors.YELLOW}  -------------{Colors.RESET}")
            print(f"{Colors.YELLOW} |{Colors.RESET}", end="")
            
            for j in range(3):
                cell = self.board[i * 3 + j]
                if cell == 'X':
                    print(f" {Colors.BLUE}{Colors.BOLD}X{Colors.RESET} {Colors.YELLOW}|{Colors.RESET}", end="")
                elif cell == 'O':
                    print(f" {Colors.RED}{Colors.BOLD}O{Colors.RESET} {Colors.YELLOW}|{Colors.RESET}", end="")
                else:
                    print(f"   {Colors.YELLOW}|{Colors.RESET}", end="")
            print()
            
        print(f"{Colors.YELLOW}  -------------{Colors.RESET}")
            
    def print_board_nums(self):
        # Display the position numbers for reference
        print(f"{Colors.BOLD}Position Numbers:{Colors.RESET}")
        
        for i in range(3):
            print(f"{Colors.CYAN}  -------------{Colors.RESET}")
            print(f"{Colors.CYAN} |{Colors.RESET}", end="")
            
            for j in range(3):
                position = i * 3 + j + 1
                print(f" {Colors.PURPLE}{position}{Colors.RESET} {Colors.CYAN}|{Colors.RESET}", end="")
            print()
            
        print(f"{Colors.CYAN}  -------------{Colors.RESET}")
    
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
    
def play_game(game, x_player, o_player, print_game=True):
    handle_quit()
    # Play a game of tic tac toe
    if print_game:
        clear_screen()
        print_title()
        print(f"{Colors.BOLD}Let's play Tic-Tac-Toe!{Colors.RESET}")
        
        game.print_board_nums()
        print()
        game.print_board()
        print()
        
    letter = 'X'  # starting letter
    turn_count = 0
    
    # Iterate while there are empty squares
    while game.empty_squares():
        turn_count += 1
        
        # Get move based on current player
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
            
        # Make move
        if game.make_move(square, letter):
            if print_game:
                clear_screen()
                print_title()
                print(f"{Colors.BOLD}Turn {turn_count}:{Colors.RESET}")
                
                player_type = "Human" if isinstance(x_player if letter == 'X' else o_player, HumanPlayer) else "AI"
                
                if letter == 'X':
                    print(f"{Colors.BLUE}{Colors.BOLD}{player_type} ({letter}){Colors.RESET} makes a move to position {square+1}")
                else:
                    print(f"{Colors.RED}{Colors.BOLD}{player_type} ({letter}){Colors.RESET} makes a move to position {square+1}")
                
                print()
                game.print_board_nums()
                print()
                game.print_board()
                print()
                
            # Check for winner
            if game.current_winner:
                if print_game:
                    player_type = "Human" if isinstance(x_player if letter == 'X' else o_player, HumanPlayer) else "AI"
                    
                    if letter == 'X':
                        print(f"\n{Colors.BLUE}{Colors.BOLD}{player_type} ({letter}) WINS!{Colors.RESET} 🎉\n")
                    else:
                        print(f"\n{Colors.RED}{Colors.BOLD}{player_type} ({letter}) WINS!{Colors.RESET} 🎉\n")
                return letter
                
            # Switch players
            letter = 'O' if letter == 'X' else 'X'
            
            # Add a slight delay for better user experience for AI moves
            if print_game and not isinstance(x_player if letter == 'X' else o_player, HumanPlayer):
                time.sleep(0.8)
                
    # If we get here, the game is a tie
    if print_game:
        print(f"{Colors.YELLOW}{Colors.BOLD}It's a TIE!{Colors.RESET} 🤝\n")