import time

from game import utilities, tictactoe, user_interface

def main(game, x_player, o_player, print_game=True):
    # Play a game of tic tac toe
    if print_game:
        print('Position numbers:')
        game.print_board_nums()
        print('\nStarting board:')
        game.print_board()
        print('')
        
    letter = 'X'  # starting letter
    
    # Iterate while there are empty squares
    while game.empty_squares():
        # Get move based on current player
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
            
        # Make move
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square+1}')  # Display 1-9 to match board
                game.print_board()
                print('')  # Empty line
                
            # Check for winner
            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter
                
            # Switch players
            letter = 'O' if letter == 'X' else 'X'
            
            # Add a slight delay for better user experience
            if print_game:
                time.sleep(0.8)
                
    # If we get here, the game is a tie
    if print_game:
        print('It\'s a tie!')

def main():
    play_again = True
    
    while play_again:
        utilities.clear_screen()
        user_interface.print_title()
        
        x_player, o_player = utilities.choose_symbol()
        t = tictactoe.TicTacToe()
        tictactoe.play_game(t, x_player, o_player, print_game=True)
        
        while True:
            again = input(f"Play again? {user_interface.Colors.CYAN}(y/n){user_interface.Colors.RESET}: ").lower()
            if again == 'y':
                break
            elif again == 'n':
                play_again = False
                break
            else:
                print(f"{user_interface.Colors.YELLOW}Invalid input. Please enter 'y' or 'n'.{user_interface.Colors.RESET}")
    
    print(f"\n{user_interface.Colors.GREEN}{user_interface.Colors.BOLD}Good Game!{user_interface.Colors.RESET}\n")

if __name__ == '__main__':
    main()