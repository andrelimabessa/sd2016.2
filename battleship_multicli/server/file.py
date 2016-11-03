from common.common import Common
from common.file import File


class ServerFile(object):
    FORMAT = 'json'
    FILE_NAME = '%s%s%s' % ('data', '.', FORMAT)
    DIR_NAME = 'server'

    def __init__(self):
        self.base_dir = File.join_path(a=Common.DATA_FOLDER_NAME, b=ServerFile.DIR_NAME)

    def get_base_dir(self, key):
        return File.join_path(a=self.base_dir, b=key)

    def get_file_name(self, key):
        return File.join_path(a=self.get_base_dir(key=key), b=ServerFile.FILE_NAME)

    def create_files_if_needed(self, key):
        if not File.exists(name=self.base_dir):
            File.mkd(name=self.base_dir)

        base_dir = self.get_base_dir(key=key)
        if not File.exists(name=base_dir):
            File.mkd(name=base_dir)

        file_name = self.get_file_name(key=key)
        if not File.exists(name=file_name):
            File.create(name=file_name)

    def has_data(self, key):
        return File.exists_and_has_content(name=self.get_file_name(key=key))

    def load_as_json(self, key):
        self.create_files_if_needed(key=key)
        return File.load_as_json(name=self.get_file_name(key=key))

    def save(self, key, data):
        self.create_files_if_needed(key=key)
        File.write_as_json(name=self.get_file_name(key=key), data=data)

    def restart_all(self, key, data):
        self.remove(key=key)
        self.create_files_if_needed(key=key)
        self.save(key=key, data=data)

    def remove(self, key):
        if self.has_data(key=key):
            File.delete(name=self.get_file_name(key=key))
            File.delete(name=self.get_base_dir(key=key))
