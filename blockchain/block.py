import hashlib


class Block():
    def __init__(self, data):
        self.hash = hashlib.sha256()
        self.nonc = 0
        self.data = data

    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.nonc += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def __str__(self):
        return "{}{}".format(self.data, self.nonc)
