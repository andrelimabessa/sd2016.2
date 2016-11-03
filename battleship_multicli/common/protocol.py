class Protocol(object):
    class Request(object):
        CONNECT = 1
        SAVE_BOARD = 2
        LOAD_BOARD = 3
        MOVE = 4
        DISCONNECT = 5

    class Response(object):
        STATUS_FAILED = 0
        STATUS_SUCCESS = 1
        STATUS_AWAITING = 2
