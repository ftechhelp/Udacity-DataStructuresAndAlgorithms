import hashlib
import uuid
from collections import OrderedDict

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = f"{self.timestamp}{self.data}{self.previous_hash}".encode()

        sha.update(hash_str)

        return sha.hexdigest()
    
class Blockchain:

    def __init__(self):
        self.chain = OrderedDict()

    def add_block(self, data):
        previous_hash = None if len(self.chain) == 0 else list(self.chain.values())[-1].hash
        new_block = Block(uuid.uuid1().time, data, previous_hash)
        self.chain[new_block.hash] = new_block

    def get_blockchain(self):
        return self.chain
    
    def get_block_by_hash(self, hash):

        if hash in self.chain:
            return self.chain[hash]
        else:
            return None

    def get_block_by_index(self, index):

        if type(index) == int and index >= 0 and index < len(self.chain):
            return list(self.chain.values())[index]
        else:
            return None
        
    def validate_chain(self):

        for index in range(1, len(self.chain)):
            current_block = list(self.chain.values())[index]
            previous_block = list(self.chain.values())[index - 1]

            if current_block.hash != current_block.calc_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
            
        return True
    
    def update_block_without_fixing_chain(self, hash, data):
        self.chain[hash].data = data
    
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1: Basic Functionality
blockchain = Blockchain()

blockchain.add_block(000)
blockchain.add_block(100)
blockchain.add_block(200)
blockchain.add_block(300)
blockchain.add_block(400)

assert blockchain.get_block_by_index(2).data == 200
assert blockchain.get_block_by_index(3).data == 300
assert blockchain.get_block_by_index(4).data == 400

block_0_hash = blockchain.get_block_by_index(0).hash
block_1_hash = blockchain.get_block_by_index(1).hash

assert blockchain.get_block_by_hash(block_0_hash).data == 000

assert blockchain.validate_chain() == True

## Test Case 2: Broken Validation
blockchain.update_block_without_fixing_chain(block_1_hash, 800)
updated_block = blockchain.get_block_by_index(1)

assert blockchain.validate_chain() == False

blockchain.update_block_without_fixing_chain(block_1_hash, 100)

assert blockchain.validate_chain() == True

## Test Case 3: Invalid Values
assert blockchain.get_block_by_hash("shjdghjsdfghdjsf") == None
assert blockchain.get_block_by_index("fhjdshfkjsdf") == None
assert blockchain.get_block_by_index(9) == None