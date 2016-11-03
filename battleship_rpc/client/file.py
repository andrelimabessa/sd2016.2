from common.common import Common
from common.file import File

class ClientFile(object):
    FORMAT = 'json'
    FILE_NAME = '%s%s%s' % ('data', '.', FORMAT)
    DIR_NAME = 'client'

    def __init__(self, _id):
        self.id = _id
        self.base_dir = File.join_path(a=Common.DATA_FOLDER_NAME, b=ClientFile.DIR_NAME)
        self.profile_dir = File.join_path(a=self.base_dir, b=self.id)
        self.data_file_name = File.join_path(a=self.profile_dir, b=ClientFile.FILE_NAME)

    def create_files_if_needed(self):
        if not File.exists(name=self.base_dir):
            File.mkd(name=self.base_dir)
        if not File.exists(name=self.profile_dir):
            File.mkd(name=self.profile_dir)
        if not File.exists(name=self.data_file_name):
            File.create(name=self.data_file_name)

    def save_state(self, state):
        self.create_files_if_needed()
        File.write_as_json(name=self.data_file_name, data=state)

    def has_data(self):
        return File.exists_and_has_content(name=self.data_file_name)

    def load_state(self):
        return File.load_as_json(name=self.data_file_name)
