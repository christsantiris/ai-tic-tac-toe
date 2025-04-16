import time

from game import utilities, tictactoe, user_interface

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