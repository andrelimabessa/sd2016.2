class InvalidRowException(Exception):
    def __init__(self, row_value):
        super(InvalidRowException, self).__init__('Linha inválida! \"%s\"' % str(row_value))
