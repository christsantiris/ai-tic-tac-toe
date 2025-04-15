import random

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (1-9): ')
            try:
                val = int(square) - 1  # Convert from 1-9 to 0-8
                if val < 0 or val > 8:
                    raise ValueError
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        # Random selection from available moves
        square = random.choice(game.available_moves())
        print(f"Computer ({self.letter}) selects position {square+1}")
        return square

class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        # First move randomly if board is empty
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # Use minimax algorithm to find best move
            square = self.minimax(game, self.letter)['position']
        print(f"Computer ({self.letter}) selects position {square+1}")
        return square
    
    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'  # the other player
        
        # First check if the previous move is a winner
        if state.current_winner == other_player:
            # Return position and score for this move
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():  # no empty squares
            return {'position': None, 'score': 0}
            
        if player == max_player:
            # Initialize for maximizing player
            best = {'position': None, 'score': -float('inf')}
        else:
            # Initialize for minimizing player
            best = {'position': None, 'score': float('inf')}
            
        for possible_move in state.available_moves():
            # Try a move
            state.make_move(possible_move, player)
            
            # Recurse using minimax to simulate game
            sim_score = self.minimax(state, other_player)
            
            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # Update best if needed
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
        return best