import json
import os


class File(object):
    @staticmethod
    def is_file(name):
        return os.path.isfile(name)

    @staticmethod
    def is_directory(name):
        return os.path.isdir(name)

    @staticmethod
    def exists(name):
        return File.is_file(name=name) or File.is_directory(name=name)

    @staticmethod
    def has_content(name):
        return os.stat(name).st_size > 0

    @staticmethod
    def exists_and_has_content(name):
        return File.exists(name=name) and File.has_content(name=name)

    @staticmethod
    def create(name):
        open(name, 'x').close()

    @staticmethod
    def load_content(name):
        with open(file=name, mode='r') as file:
            return file.read()

    @staticmethod
    def delete(name):
        if File.is_file(name=name):
            os.remove(name)
        elif File.is_directory(name=name):
            os.rmdir(name)

    @staticmethod
    def mkd(name):
        if not File.exists(name=name):
            os.makedirs(name)

    @staticmethod
    def load_as_json(name):
        return json.loads(s=File.load_content(name=name))

    @staticmethod
    def write_as_json(name, data):
        with open(name, 'w') as outfile:
            json.dump(obj=data, fp=outfile, indent=4, sort_keys=False, separators=(',', ':'))

    @staticmethod
    def join_path(a, b):
        return os.path.join(a, b)
