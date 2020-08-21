#Blockchain example

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask

class Blockchain(object):
    """stores transactions, adds new blocks to the chain"""
    def __init__(self):
        self.chain= []
        self.current_transactions = []

        #creates genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash= None):
        """creates new block and adds it to the chain
        proof: proof given by proof of work algorithm (int)
        previous hash: (optional) hash of previous block (str)
        return: New Block (dict)"""
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #rests current list of transactions
        self.current_transactions=[]
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """adds a new transaction to the list of transactions
        sender: address of the sender (str)
        recipient: address of recipient
         amount: amount (integer)
         returns the index of the Block that will hold this transaction"""
        self.current_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
        })

        return self.last_block['index']+1 #returns index of the block where the transaction will be added

    @property
    def last_block(self):
        # returns last block in the chain
        return self.chain[-1]

    @staticmethod
    #remember, static methods are "general" methods for a class
    #don't depend on whether there is an instance of the class or not
    def hash(block):
        """creates a SHA-256 hash of a Block
        block: Block(dict)
        returns str"""

        #makes sure the Dictionary is ordered
        block_string = json.dumps(block, sort_keys=True).encode
        return hashlib.sha256(block_string).hexdigest()
        pass

    def proof_of_work(self, last_proof):
        """
        a simple proof of work algorithm
        -find a number p' such that hash (pp') contains leading 4 zeroes
        (where p is the previous proof, p' is the new proof)
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof+=1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """valides the proof:
        sees if pp' plugged into the hash function contains 4 leading zeros?
        lastproof: previous proof
        proof: current proof
        return True if correct, else False"""

        guess =f'{last+proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
from hashlib import sha256
x=5
y= 0 #trying to find y



# Notes:
# PoW is how new Blocks are mined on the blockchain
#   goal of PoW is to discover a number which solves a problem
# the number should be difficult to find but easy to verify
#e.g.
# hash of some integer x multiplied by another y must end in 0
# hash (x *y) = #
"""
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != '0':
#while the last element of x*y doesn't hash to equal 0
    y+=1
print(f'the solution is y= {y}')
"""


