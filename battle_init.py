# -*- coding: utf-8 -*-

from battle_ship import BattleShip
from console import Console


class Opcoes(object):
    move="1"
    restart="2"
    game="3"
    board="4"
    clear="5"
    exit="6"
    def __init__(self):
        pass

class BattleInit(object):
    def __init__(self):
        #instancia Jogo BattleShip
        self.battle = BattleShip()

    def mostrar_legenda(self):
        print("------------------------")
        print(" 🌊 = Água")
        print(" 🚤 = Navio")
        print(" 🚩 = Abatido")
        print(" 💣 = Bomba")
        print("------------------------")

    def mostrar_opcoes(self):
        print("|------------------ OPÇÕES ---------------------------|")
        print("|-1 -> SAIR                                           |")
        print("|-2 -> JOGAR                                          |")
        print("|-3 -> MOSTRAR JOGO                                   |")
        print("|-4 -> MOSTRAR TABULEIRO                              |")
        print("|-5 -> REINICIAR                                      |")
        print("|-6 -> clear                                          |")
        print("|-----------------------------------------------------|", end="\n\n")

    def mover(self):
        self.battle.mostrar_tabuleiro()
        l = input("\nInforme posição(x,y):\n")
        #c = input("\nInforme:\n")
        self.battle.move(int(l), int(c))


    def mostrar_tabuleiro(self):
        self.mostrar_legenda()
        print("------------------------")
        print("------- Tabuleiro ------")
        print("------------------------", end="\n")
        for x in range(self.rows):
            print("| ", end="")
            for y in range(self.cols):
                value = self.game[x][y]
                if value == Objeto.agua or value == Objeto.navio:
                    print(" 🌊 ", end=" ")
                elif value == Objeto.abatido:
                    print(" 🚩 ", end=" ")
                else:
                    print(" 💣 ", end=" ")
            print(" |", end="\n")
        print("------------------------")

    def iniciar(self):
        self.mostrar_opcoes()
        c = input("Informe a opção:\n")

        while c != Opcoes.clear:
 
            Console.clear()
            self.battle.move_count()

            if c == Opcoes.move:
                self.mover()

            elif c == Opcoes.board:
                self.battle.mostrar_tabuleiro()

            elif c == Opcoes.game:
                self.battle.mostrar_jogo()

            elif c == Opcoes.reiniciar:
                self.battle.reiniciar_game()
                Console.clear()
                self.battle.mostrar_tabuleiro()

            elif c == Opcoes.clear:
                Console.clear()

            else:
               print("Opção inválida!")

            self.mostrar_opcoes()

            c = input("Escolha a opcão desejada\n")

        print("Tchau! :)")
