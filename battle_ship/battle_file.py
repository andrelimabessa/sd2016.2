import os
import json


class Info:
    file = "battleship.json" # ARQUIVO
    dir = "db" # DIRETORIO
    def __init__(self):
        pass

class Database(object):
    def __init__(self):
        self.file = os.path.join(Info.dir, Info.file)
        self.validate()

    def validate(self):
        if not os.path.exists(Info.dir):
            os.makedirs(Info.dir)
        if not os.path.isfile(self.file):
            open(self.file, 'x').close()

    def has_saved(self):
        return os.path.isfile(self.file) and os.stat(self.file).st_size > 0

    def get_saved(self):
        with open(self.file, 'r') as file:
            return json.loads(file.read())

    def restart(self, db):
        self.remove()
        self.validate()
        self.save(db)

    def save(self, db):
        with open(self.file, 'w') as outfile:
            json.dump(db, outfile, indent=4, sort_keys=False, separators=(',', ':'))

    def remove(self):
	    if self.has_saved():
	        os.remove(os.path.join(Info.dir, Info.file))
	        os.rmdir(Info.dir)
