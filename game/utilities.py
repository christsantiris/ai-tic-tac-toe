import os
from players.players import RandomComputerPlayer, AIComputerPlayer, HumanPlayer
from game.user_interface import Colors

def choose_player():
    print(f"{Colors.BOLD}Select your opponent:{Colors.RESET}")
    print(f"1. {Colors.GREEN}Random AI{Colors.RESET} (Easy difficulty)")
    print(f"2. {Colors.RED}Smart AI{Colors.RESET} (Impossible to beat)")
    
    while True:
        choice = input(f"\nEnter your choice {Colors.CYAN}(1 or 2){Colors.RESET}: ")
        if choice == '1':
            return RandomComputerPlayer('O')
        elif choice == '2':
            return AIComputerPlayer('O')
        else:
            print(f"{Colors.YELLOW}Invalid choice. Please enter 1 or 2.{Colors.RESET}")

def choose_symbol():
    print(f"{Colors.BOLD}Do you want to play as X or O?{Colors.RESET}")
    print(f"{Colors.BLUE}X{Colors.RESET} goes first, {Colors.RED}O{Colors.RESET} goes second.")
    
    while True:
        choice = input(f"\nEnter your choice {Colors.CYAN}(X or O){Colors.RESET}: ").upper()
        if choice == 'X':
            return HumanPlayer('X'), choose_player()
        elif choice == 'O':
            ai_type = choose_player()
            ai_type.letter = 'X'
            return ai_type, HumanPlayer('O')
        else:
            print(f"{Colors.YELLOW}Invalid choice. Please enter X or O.{Colors.RESET}")

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_quit():
    """Set up signal handlers to gracefully quit the game with keyboard shortcuts."""
    import signal
    import sys
    
    def signal_handler(sig, frame):
        print(f"\n\n{Colors.YELLOW}{Colors.BOLD}Game Quit. Thanks for playing!{Colors.RESET}")
        sys.exit(0)
    
    # Register the signal handler for CTRL+C (SIGINT)
    signal.signal(signal.SIGINT, signal_handler)
    
    # On Windows, CTRL+Break is SIGBREAK
    if hasattr(signal, 'SIGBREAK'):  # Windows only
        signal.signal(signal.SIGBREAK, signal_handler)
    
    # On Unix systems, register for SIGTERM as well
    if hasattr(signal, 'SIGTERM'):
        signal.signal(signal.SIGTERM, signal_handler)