class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[47m'
    BLACK = '\033[30m'

def print_title():
    # Print a fancy title
    title = r"""
 _____ _     _____         _____         
|_   _(_) __|_   _|_ _  __|_   _|__  ___ 
  | | | |/ __|| |/ _` |/ __|| |/ _ \/ _ \
  | | | | (__ | | (_| | (__ | | (_)|| __/
  |_| |_|\___||_|\__,_|\___||_|\___/\___|
                                         
"""
    print(f"{Colors.CYAN}{title}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}A game of X's and O's with AI opponents{Colors.RESET}")
    print()