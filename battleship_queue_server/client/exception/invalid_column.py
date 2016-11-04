class InvalidColumnException(Exception):
    def __init__(self, column_value):
        super(InvalidColumnException, self).__init__('Coluna inválida! \"%s\"' % str(column_value))
