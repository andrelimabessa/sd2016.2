# -*- coding: utf-8 -*-
from random import randint
from battle_leg import Leg
from battle_file import Database

class BattleShip(object):

    def __init__(self):
        self.database = Database()
        self.load(False)
        self.save()

    def load(self, is_new_game):
        if self.database.has_saved():
            print("Recuperando!")
        else:
            print("Novo!")

        if self.database.has_saved() and not is_new_game:
            state = self.database.get_saved()
        else:
            state = self.get_default_state()

        self.rows = state["rows"]
        self.cols = state["cols"]
        self.game_board = state["game_board"]
        self.max_move = state["max_move"]
        self.current_move_count = state["current_move_count"]

    def reiniciar(self):
	    self.load(is_new_game=True)
	    self.database.restart(self.get_state())

    def salvar(self):
        self.database.save_game(self.get_state())

    def status(self):
        return {
            "rows": self.rows,
            "cols": self.cols,
            "max_move": self.max_move,
            "game_board": self.game_board,
            "current_move_count": self.current_move_count
        }

    def status_default(self):
        return {
            "rows": 5,
            "cols": 5,
            "max_move": 5,
            "game_board": self.create_game_board(5, 5),
            "current_move_count": 0
        }

"""
	AGUA = 'A'
	NAVIO = 'N'
	ABATIDO ='B'

	def init_tab(self):
		self.matrix = [[self.AGUA for i in range(5)] for j in range(5)]

	def print_tab(self):
		print(self.matrix)

	def set_navios(self,x,y):
		self.matrix[x][y] = self.NAVIO

	def jogada(self, x, y):
		if self.matrix[x][y] == self.NAVIO:
			self.matrix[x][y] = self.ABATIDO
			print("Navio abatido")
		else:
			print('Água')
		print(self.matrix)			

b = buttleship()
b.init_tab()
#b.print_tab()
b.set_navios(0,0)
b.set_navios(3,3)
b.jogada(1,2)
b.print_tab()
b.jogada(3,3)
b.print_tab()
"""