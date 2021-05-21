from hashlib import sha256
import json
from datetime import datetime

class Block:
    def __init__(self, i, prevHash, transactions, timestamp, nonce):
        self.i = i
        self.prevHash = prevHash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.hashcode()

    def hashcode(self):
        return sha256(sha256(json.dumps(self.__dict__, sort_keys=True).encode()).hexdigest().encode()).hexdigest()

    def __str__(self):
        return str(self.__dict__)