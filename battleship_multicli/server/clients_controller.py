class ClientsController(object):
    @staticmethod
    def is_active(_id, active):
        for pair in active:
            if pair[0][0] == _id or pair[1][0] == _id:
                return True
        return False

    @staticmethod
    def get_pair(_id, active):
        for pair in active:
            if pair[0][0] == _id or pair[1][0] == _id:
                return pair
        return None

    @staticmethod
    def remove_pair(_id, active):
        active.remove(ClientsController.get_pair(_id=_id, active=active))

    @staticmethod
    def resolve_storage_key(_id, pair, storage):
        first_key = '%s_%s' % (str(_id), str(ClientsController.get_other_id(pair=pair, _id=_id)))
        second_key = '%s_%s' % (str(ClientsController.get_other_id(pair=pair, _id=_id)), str(_id))

        if storage.has_data(key=second_key):
            return second_key
        return first_key

    @staticmethod
    def get_other_id(pair, _id):
        if pair[0][0] == _id:
            return pair[1][0]
        else:
            return pair[0][0]

    @staticmethod
    def get_address(pair, _id):
        if pair[0][0] == _id:
            return pair[0][1]
        else:
            return pair[1][1]

    @staticmethod
    def get_other_address(pair, _id):
        if pair[0][0] == _id:
            return pair[1][1]
        else:
            return pair[0][1]
