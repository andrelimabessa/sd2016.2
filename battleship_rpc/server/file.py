from common.common import Common
from common.file import File


class ServerFile(object):
    FORMAT = 'json'
    FILE_NAME = '%s%s%s' % ('data', '.', FORMAT)
    DIR_NAME = 'server'

    def __init__(self):
        self.base_dir = File.join_path(a=Common.DATA_FOLDER_NAME, b=ServerStorage.DIR_NAME)

    def get_base_dir(self, _id):
        return File.join_path(a=self.base_dir, b=_id)

    def get_file_name(self, _id):
        return File.join_path(a=self.get_base_dir(_id=_id), b=ServerStorage.FILE_NAME)

    def create_files_if_needed(self, _id):
        if not File.exists(name=self.base_dir):
            File.mkd(name=self.base_dir)

        base_dir = self.get_base_dir(_id=_id)
        if not File.exists(name=base_dir):
            File.mkd(name=base_dir)

        file_name = self.get_file_name(_id=_id)
        if not File.exists(name=file_name):
            File.create(name=file_name)

    def has_data(self, _id):
        return File.exists_and_has_content(name=self.get_file_name(_id=_id))

    def load_as_json(self, _id):
        self.create_files_if_needed(_id=_id)
        return File.load_as_json(name=self.get_file_name(_id=_id))

    def save(self, _id, data):
        self.create_files_if_needed(_id=_id)
        File.write_as_json(name=self.get_file_name(_id=_id), data=data)

    def restart_all(self, _id, data):
        self.remove(_id=_id)
        self.create_files_if_needed(_id=_id)
        self.save(_id=_id, data=data)

    def remove(self, _id):
        if self.has_data(_id=_id):
            File.delete(name=self.get_file_name(_id=_id))
            File.delete(name=self.get_base_dir(_id=_id))
