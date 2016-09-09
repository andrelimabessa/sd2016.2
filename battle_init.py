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
        print(" ~ = Água")
        print(" v = Navio")
        print(" a = Abatido")
        print(" b = Bomba")
        print("------------------------")

    def mostrar_opcoes(self):
        print("|------------------ OPÇÕES ---------------------------|")
        print("|-1 -> MOVER                                          |")
        print("|-2 -> JOGAR                                          |")
        print("|-3 -> MOSTRAR JOGO                                   |")
        print("|-4 -> MOSTRAR TABULEIRO                              |")
        print("|-5 -> REINICIAR                                      |")
        print("|-6 -> SAIR                                           |")
        print("|-----------------------------------------------------|", end="\n\n")

    def mover(self):
        self.mostrar_legenda()
        self.battle.mostrar_tabuleiro()
        l = input("\nInforme posição(x,y):\n")
        #c = input("\nInforme:\n")
        self.battle.move(int(l), int(c))


    def iniciar(self):
        self.mostrar_opcoes()
        c = input("Informe a opção:\n")

        while c != Opcoes.clear:
 
            Console.clear()
            self.battle.move_count()

            # OPÇÃO 1
            if c == Opcoes.move:
                self.mover()

            elif c == Opcoes.board:
                self.battle.mostrar_tabuleiro()

            elif c == Opcoes.game:
                self.battle.mostrar_jogo()

            # OPÇÃO 5
            elif c == Opcoes.reiniciar:
                self.battle.reiniciar_game()
                Console.clear()
                self.battle.mostrar_tabuleiro()

            elif c == Opcoes.clear:
                Console.clear()
            # OPÇÃO 6 - SAIR
            else:
               print("Opção inválida! \n")

            self.mostrar_opcoes()

            c = input("Informe uma opção: \n")

        print("Tchau! :)")
