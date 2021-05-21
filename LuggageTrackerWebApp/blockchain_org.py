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

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.transactions=[]
        self.genesisBlock()

    def __str__(self):
        return str(self.__dict__)

    def genesisBlock(self):
        genesis_block=Block('Genesis',0x0,[3,4,5,6,7],'datetime.now().timestamp()',0)
        genesis_block.hash=genesis_block.hashcode()
        self.chain.append(genesis_block.hash)
        self.transactions.append(str(genesis_block.__dict__))
        return genesis_block

    def getLastBlock(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        difficulty = 1
        block.nonce = 0
        computed_hash = block.hashcode()
        while not (computed_hash.endswith('0' * difficulty) and ('55' * difficulty) in computed_hash):
            block.nonce += 1
            computed_hash =  block.hashcode()
        return computed_hash

    def add(self, data):
        block=Block(len(self.chain), self.chain[-1], data, 'datetime.now().timestamp()', 0)
        block.hash = self.proof_of_work(block)
        self.chain.append(block.hash)
        self.transactions.append(block.__dict__)
        return json.loads(str(block.__dict__).replace('\'','\"'))
        

    def getTransactions(self, id):
        labels=['pending','transit','arrived'] 
        while True:
            try:
                if id == 'all':
                    for i in range(len(self.transactions)-1):
                        print('{}:\n{}\n'.format(labels[i],self.transactions[i+1]))
                    break

                elif type(id) == int:
                    print(self.transactions[id])
                    break

            except Exception as e:
                print(e)


def main():
    manufacturer={
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial': 50001000,
                'name': 'Kalgis luggage',
                'from': 'Airline X',
                'to': 'Airline Y',
                'message': 'Found at Ohare',
                'digital signature': 'approved',
                'flagged': 'N'
                }
            ]
        }
    transportation={
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial': 50001000,
                'name': 'Kalgis luggage',
                'from': 'Airline X',
                'to': 'Airline Y',
                'message': 'Found at Ohare',
                'digital signature': 'approved',
                'flagged': 'N'
                }
            ]
        }
    retailer={
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial': 50001000,
                'name': 'Kalgis luggage',
                'from': 'Airline X',
                'to': 'Airline Y',
                'message': 'Found at Ohare',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial': 50001000,
                'name': 'Kalgis luggage',
                'from': 'Airline X',
                'to': 'Airline Y',
                'message': 'Found at Ohare',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':3,
                'product_serial': 50001000,
                'name': 'Kalgis luggage',
                'from': 'Airline X',
                'to': 'Airline Y',
                'message': 'Found at Ohare',
                'digital signature': 'approved',
                'flagged': 'N'
                }
            ]
        }
    
    B = Blockchain()
    a = B.add(manufacturer)
    b = B.add(transportation)
    c = B.add(retailer)
    B.getTransactions('all')

if __name__=='__main__':
    main()
    








