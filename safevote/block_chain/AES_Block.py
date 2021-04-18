import hashlib
import sys 
import select
from base64 import b64decode, b64decode
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AES_Block:


    def __init__(self, user_id, vote, previous_block = None, IV = None):
        self.key = hashlib.sha256(get_random_bytes(16)).digest() # Each block will have it's own random cipher key

        if previous_block: # Checks to ensure it isn't the first block
            self.previous_block = previous_block
            self.data = (previous_block.block + "USER/VOTE," + user_id.decode("utf8") + "/" + vote.decode("utf8")) #Data of block chain is previous_block plus data of new block 
            
        else:
            self.data = ("USER/VOTE,"+ user_id.decode("utf8") + "/" + vote.decode("utf8"))
            self.previous_block = None
    

        if IV: # If it is the first block then there is an Initilization Vector
            self.IV = IV

        else:
            self.IV = None
           

        self.e_cipher = AES.new(self.key, AES.MODE_CBC, IV)

        

        self.block = self.e_cipher.encrypt(pad(self.data.encode("utf8"), AES.block_size)) #Encrypt the data
        #self.block = self.e_cipher.encrypt(self.data, AES.block_size)

    def Decrypt_Block(self):

        decrypted_block = ""
    
        if self.IV:
            self.d_cipher = AES.new(self.key, AES.MODE_CBC, self.IV)   
            
             
        else:
            self.d_cipher = AES.new(self.key, AES.MODE_CBC)
          
     
        decrypted_block = unpad (self.d_cipher.decrypt(self.block), AES.block_size)


        return decrypted_block

