class Protocol(object):
    class Request(object):
        CONNECT = 1
        SAVE_BOARD = 2
        LOAD_BOARD = 3

    class Response(object):
        STATUS_SUCCESS = 1
        STATUS_FAILED = 0
