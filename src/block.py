import time
import json
from Crypto.Hash import SHA256
from parameters import DIFFICULTY
 
class Block:
    def __init__(self, index, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = []
        self.nonce = 0
        self.current_hash = None
        self.previous_hash = previous_hash
        
    def create_hash_object(self):
        temp = self.__dict__.copy()
        temp.pop("current_hash", None)

        hashable = json.dumps(temp, sort_keys=True).encode()
        return SHA256.new(hashable)

    def mine_block(self):
        while self.create_hash_object().hexdigest()[:DIFFICULTY] != '0' * DIFFICULTY:
            self.nonce += 1
        self.current_hash = self.create_hash_object()
        return self

# block = Block(0, -1)
# print(block.mine_block().current_hash)