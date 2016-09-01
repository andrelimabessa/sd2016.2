# -*- coding: utf-8 -*-
from random import randint
from battle_obj import Objeto
from battle_file import Database

class BattleShip(object):

    def __init__(self):
        self.database = Database()
        self.load(False)
        self.salvar()

    def load(self, is_new_game):
        if self.database.has_saved():
            print("Jogo Recuperado!")
        else:
            print("Novo jogo!")

        if self.database.has_saved() and not is_new_game:
            state = self.database.get_saved()
        else:
            state = self.default_state()

        self.rows = state["rows"]
        self.cols = state["cols"]
        self.board = state["board"]
        self.max = state["max"]
        self.count = state["count"]

    def reiniciar(self):
	    self.load(is_new_game=True)
	    self.database.restart(self.state())

    def salvar(self):
        self.database.save(self.state())

    def criar_tabuleiro(self, rows, cols):
        tab = [[Objeto.agua for x in range(rows)] for y in range(cols)]
        for i in range(int((rows * cols) / 2)):
            tab[randint(0, 4)][randint(0, 4)] = Objeto.navio
        return tab

    def state(self):
        return {
            "rows": self.rows,
            "cols": self.cols,
            "max": self.max,
            "board": self.board,
            "count": self.count
        }

    def default_state(self):
        return {
            "rows": 5,
            "cols": 5,
            "max": 5,
            "board": self.criar_tabuleiro(5, 5),
            "count": 0
        }

