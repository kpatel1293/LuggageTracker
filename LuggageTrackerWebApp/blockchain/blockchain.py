from hashlib import sha256
import time
import json

class Block:
    def __init__(self, index, transactions, timestamp, prevHash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.nonce = nonce

    def computeHash(self):
        return sha256(sha256(json.dumps(self.__dict__, sort_keys=True).encode()).hexdigest().encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.genesisBlock()

    def genesisBlock(self):
        genesisBlock = Block(0, ['Genesis Block'], time.time(), '0')
        genesisBlock.hash = genesisBlock.computeHash()
        self.chain.append(genesisBlock)

    @property
    def lastBlock(self):
        return self.chain[-1]
    
    difficulty = 2
    def proofOfWork(self, block):
        block.nonce = 0
        computedHash = block.computeHash()
        while not computedHash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computedHash = block.computeHash()
        return computedHash
    
    def addBlock(self, block, proof):
        if self.lastBlock.hash != block.prevHash or not self.checkProof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def checkProof(self, block, blockHash):
        return (blockHash.startswith('0' * Blockchain.difficulty) and blockHash == block.computeHash())
    
    def blockchainTransactions(self, transaction):
        self.transactions.append(transaction)
    
    def mine(self):
        if not self.transactions:
            return False
        
        lastBlock = self.lastBlock

        newBlock = Block(index=lastBlock.index + 1, transactions=self.transactions, timestamp=time.time(), prevHash=lastBlock.hash)

        proof = self.proofOfWork(newBlock)
        self.addBlock(newBlock, proof)
        self.transactions = []
        return newBlock.index

    def getSize(self):
        return len(self.chain)