import json
from common.common import Common

class Serializer(object):
    @staticmethod
    def to_binary_json(data):
        return json.dumps(data).encode(Common.ENCODE)

    @staticmethod
    def from_binary_json(data):
        return json.loads(data.decode(Common.ENCODE))
