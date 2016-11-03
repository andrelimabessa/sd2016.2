from common.common import Common


class Printer(object):
    @staticmethod
    def print_connecting_error():
        print('An error ocurred trying to connect with server. Please, try again.')

    @staticmethod
    def print_choice():
        print('---------- BATTLE SHIP GAME ----------')
        print('1 - Jogar')
        print('2 - Mostrar Tabuleiro')
        print('3 - Mostrar Tabuleiro Real')
        print('4 - Reiniciar')
        print('5 - Limpar')
        print('6 - Exit', end='\n\n')

    @staticmethod
    def print_remaining_moves(remaining):
        print("Jogadas restantes: %s" % str(remaining), end='\n\n')

    @staticmethod
    def print_invalid_choice():
        print("Opção inválida. Tente novamente...", end='\n\n')

    @staticmethod
    def print_exception(exception):
        print(str(exception))

    @staticmethod
    def print_message(message):
        print(message)
