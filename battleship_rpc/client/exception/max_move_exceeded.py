class MaxMoveExceededException(Exception):
    def __init__(self, move):
        super(MaxMoveExceededException, self).__init__('Movimentos excedidos! \"%s\"' % str(move))
