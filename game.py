from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time
import math

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #a single list to rep 3x3 board
        self.current_winner = None

    def print_board(self):
        # This is just getting the row
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
        # for i in range(3):
        #   row = self.board[i*3 : (i+1)*3]
            print("| " + " | ".join(row) + " |")

    @staticmethod
    # Static methods are methods that belong to the class itself and not to any specific instance (object) of the class.
    # They do not have access to the instance-specific data and are independent of the state of the class or its instances.
    def print_board_num():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
            # ['x',' ','o'] --> [(0,'x'),(1,' '),(2,'o')]
        #    if spot == ' ':
        #        moves.append(i)
        # return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_square(self):
        #return len(self.available_moves())
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check the column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        #check diagonals:
        #but only if the square is an even number [0,2,4,6,8]
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_num()

    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # (we dont have to worry about winner bc we will just return that which breaks the loop)

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print("") #print an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        #tiny break
        if print_game:
            time.sleep(1)

    if print_game:
        print('It\'s a tie!')

if __name__ == "__main__":

    x_wins = 0
    o_wins = 0
    ties = 0

    for i in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game = False)

        if result == 'O':
            o_wins += 1
        elif result == 'X':
            x_wins += 1
        else:
            ties += 1

    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties.')