import hashlib
import sys 
import select
from base64 import b64decode, b64decode
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from AES_Block import AES_Block

class AES_Block_Chain:

    def __init__(self, initial_block):
        self.vote_count = 1 # account for initial vote
        self.initial_block = initial_block
        self.chain = []
        self.chain.append(initial_block)
        self.user_votes = {"name" : "vote"}
        self.votes_count = {"vote" : 0}
      
    
    def __getitem__(self, index):
        return self.chain[index]

    #Function Checks block chain integrity before adding to block chain
    def Add_Block(self, block):
        self.vote_count += 1
        if self.Check_Block_Chain():
            self.chain.append(block)
            return True
        else:
            assert ("BLOCK CHAIN TAMPERED WITH")
            return False

    #gets the current block in the block chain
    def Get_Curr_Block (self):
        return self.chain[len(self.chain)-1]

    def Get_Init_IV (self):
        return self.chain[0].IV

    #Function that individually decodes each block in the block
    #chain and sorts data into maps. NEEDS LIST OF CANDIDATES TO INITIALIZE VOTES MAP
    def Calculte_Votes(self, list_cand):

        for candidate in list_cand:
            self.votes_count[candidate] = 0
        
        for blocks in self.chain:
            decoded = blocks.Decrypt_Block()
            _ , data = decoded[decoded.index("USER/VOTE"):].split(",")
            user, vote = data.split('/')
            self.user_votes[user] = vote
            self.votes_count[vote] += 1
        
        return self.user_votes, self.votes_count

    
    # Insures the integrity of the block chain by comparing
    # a blocks previous block to the previous blocks encryption
    def Check_Block_Chain(self):
        curr = self.Get_Curr_Block()
        if len (self.chain) > 1:
            if curr.previous_block.block is not self.chain[len(self.chain) - 2].block:
                print("FOOOK") 
                return False
            else:
                return True
        else:
            return True 

        


