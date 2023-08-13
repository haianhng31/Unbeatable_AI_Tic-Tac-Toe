import math
import random

class Player():
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # players get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        # super() is a built-in function used to call a method from the parent class (also called a superclass).
        # In this context, it is calling the constructor of the parent class to perform any necessary initialization for the object.

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_quare = False
        val = None
        while not valid_quare:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_quare = True
            except ValueError:
                print('Invalid square. Try again!')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get the square based off on the MINIMAX algorithm
            square = self.minimax(game,self.letter)['position']
        return square


    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # first, we want to check if the previous move is a winner
        # this is our base case because the game has ended, and there's no need to look further into the future.
        '''if state.current_winner:
            if state.current_winner == other_player:
                return {'position': None, 'score': -1}
            if state.current_winner == max_player:
                return {'position': None, 'score': 1}'''
        if state.current_winner == other_player:
            # we should return position & score bc we need to keep track of the score for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_square() + 1) if other_player == max_player
                    else -1 * (state.num_empty_square() + 1)
                    }
            # i really don't understand the code above

        elif not state.empty_squares(): #no empty square
            return {'position': None, 'score': 0}

        #initialize some dictionaries
        if player == max_player:
            best = {'position':None,'score':-math.inf} #each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} #each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move,player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) #now we alternate players
            #sim_score = self.minimax(state, other_player if player == max_player else max_player)
            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if neccessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    ''' where does sim_score come from?? '''
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best




