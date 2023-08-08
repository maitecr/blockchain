# Module 1 - Create Blockchain

import datetime
import hashlib
import json
from Flask import Flask, jsoninfy

#Part 1: Building a block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {}


#Part 2: Mining a block