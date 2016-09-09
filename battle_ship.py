# -*- coding: utf-8 -*-
from random import randint
from battle_obj import Objeto
from battle_file import Database

class BattleShip(object):

    def __init__(self):
        self.database = Database()
        self.load(False)
        self.salvar()

    # carrega jogo, novo ou salvo
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

    # reinicia jogo
    def reiniciar(self):
	    self.load(is_new_game=True)
	    self.database.restart(self.state())

    # salva jogo em arquivo de dados
    def salvar(self):
        self.database.save(self.state())

    # cria tabuleiro
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

    # seta estado default
    def default_state(self):
        return {
            "rows": 5,
            "cols": 5,
            "max": 5,
            "board": self.criar_tabuleiro(5, 5),
            "count": 0
        }
    # mostras o total de jogadas restantes    
    def move_count(self):
        print("Restam: " + str(self.max - self.count) + " jogadas!")

    # visualiza elementos do tabuleiro
    def mostrar_tabuleiro(self):
        print("************************")
        print("------- Tabuleiro ------")
        print("************************", end="\n")
        for x in range(self.rows):
            print("| ", end="")
            for y in range(self.cols):
                value = self.board[x][y]
                if value == Objeto.agua or value == Objeto.navio:
                    print(" ~ ", end=" ")
                elif value == Objeto.abatido:
                    print(" a ", end=" ")
                else:
                    print(" n ", end=" ")
            print(" |", end="\n")
        print("------------------------")

    def move(self, x, y):
        if x - 1 < 0 or x > self.rows:
            print("x inválido: " + str(x))
        elif y - 1 < 0 or y > self.cols:
            print("y inválido: " + str(y))
        elif self.count + 1 > self.max:
            print("Limite atingido: " + str(self.max))
        else:
            self.count += 1
            x -= 1
            y -= 1
            value = self.board[x][y]
            if value == Objeto.navio or value == Objeto.abatido:
                self.board[x][y] = Objeto.abatido
            else:
                self.board[x][y] = Objeto.bomba
            self.save()        
