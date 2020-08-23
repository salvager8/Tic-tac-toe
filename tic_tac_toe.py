import subprocess as sp
import time
from termcolor import colored, cprint

class TicTacToe:
    def __init__(self):
        self.board = [None] * 9
        self.turn = 'O'
        self.turn_amount = 0
        self.win_cases = [
            [0, 3, 6],
            [0, 4, 8],
            [0, 1, 2],
            [1, 4, 7],
            [2, 4, 6],
            [2, 5, 8],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.win_condition = False

    def make_move(self, turn, position):
        self.board[position] = turn

    def _turn(self, turn):
        self.turn = 'X' if turn == 'O' else 'O'
        return self.turn
    
    def format_chars(self, char):
        if char is not None:
            return char
        return ' '
    
    def display_board(self):
        sp.call('clear', shell=True)
        print('------------------------------')
        print('\n')
        print('         |         |         ')
        print('    {0}    |    {1}    |    {2}  '.format(
            (
                self.format_chars(self.board[0])),
                self.format_chars(self.board[1]),
                self.format_chars(self.board[2])
            )
        )
        print('         |         |         ')
        print('---------|---------|---------')
        print('         |         |         ')
        print('    {0}    |    {1}    |    {2}  '.format(
            (
                self.format_chars(self.board[3])),
                self.format_chars(self.board[4]),
                self.format_chars(self.board[5])
            )
        )
        print('         |         |         ')
        print('---------|---------|---------')
        print('         |         |         ')
        print('    {0}    |    {1}    |    {2}  '.format(
            (
                self.format_chars(self.board[6])),
                self.format_chars(self.board[7]),
                self.format_chars(self.board[8])
            )
        )
        print('         |         |         ')
        print('\n')
        print('------------------------------')

    def played(self, char):
        condition = False
        if char is not None:
            condition = True
        return condition

    def check_win(self):
        for win_case in self.win_cases:
            if self.board[win_case[0]] == self.board[win_case[1]]\
                and self.board[win_case[0]] == self.board[win_case[2]]\
                and self.played(self.board[win_case[0]])\
                and self.played(self.board[win_case[1]])\
                and self.played(self.board[win_case[2]]):
                self.win_condition = True
        
    def validate_input(self, value):
        if value.isdecimal():
            if int(value) > 0 and int(value) < 10:
                return True
        else:
            return False

    def handle_error(self, err):
        self.turn_amount = self.turn_amount - 1
        self._turn(self.turn)
        cprint(err, 'red', attrs=['blink'])
        time.sleep(2)
        self.display_board()

    def start(self):
        self.display_board()
        self.turn_amount = self.turn_amount + 1
        user_input = input('Enter next move position for player \"X\": ')
        if self.validate_input(user_input):
            position = int(user_input) - 1
        else:
            self.handle_error('Please use only numbers from 1 to 9!')
            self._turn(self.turn)
            self.start()
        self.make_move(self._turn(self.turn), position)
        self.display_board()
        while(not self.win_condition and self.turn_amount < 9):
            self._turn(self.turn)
            self.turn_amount = self.turn_amount + 1
            user_input = input('Enter next move position for player \"{}\": '.format(self.turn))
            if self.validate_input(user_input):
                position = int(user_input) - 1
                if not self.played(self.board[position]):
                    self.make_move(self.turn, position)
                    self.display_board()
                    self.check_win()
                else:
                    self.handle_error('Please introduce a not played position!')
            else:
                self.handle_error('Please use only numbers from 1 to 9!')
        if self.win_condition:
            cprint('Game Ended, {} won!'.format(self.turn), 'green', attrs=['blink'])
        else:
            cprint('Game ended with a tie, please restart the game', 'white', attrs=['blink'])

game = TicTacToe()
game.start()
