from players.players import RandomComputerPlayer, SmartComputerPlayer, HumanPlayer

def choose_player():
    print("Select your opponent:")
    print("1. Random AI (easy)")
    print("2. Smart AI (impossible to beat)")
    
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            return RandomComputerPlayer('O')
        elif choice == '2':
            return SmartComputerPlayer('O')
        else:
            print("Invalid choice. Please enter 1 or 2.")

def choose_symbol():
    print("Do you want to play as X or O?")
    print("X goes first, O goes second.")
    
    while True:
        choice = input("Enter X or O: ").upper()
        if choice == 'X':
            return HumanPlayer('X'), choose_player()
        elif choice == 'O':
            ai_type = choose_player()
            ai_type.letter = 'X'
            return ai_type, HumanPlayer('O')
        else:
            print("Invalid choice. Please enter X or O.")