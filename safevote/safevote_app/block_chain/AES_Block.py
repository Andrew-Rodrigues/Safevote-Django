import hashlib
import sys 
import codecs
import select
from base64 import b64decode, b64decode
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AES_Block:


    def __init__(self, concat_data = None, previous_block = None, encrypt_data = None, IV = None, key = None):
        # self.key = hashlib.sha256(get_random_bytes(16)).digest() # Each block will have it's own random cipher key
        # self.IV = get_random_bytes(16)

        if previous_block and concat_data: # Checks to ensure it isn't the first block
            self.previous_block = previous_block
            
            self.data = (previous_block + "USER/VOTE," + concat_data.decode()) #Data of block chain is previous_block plus data of new block 
            
        elif concat_data:
            self.data = ("USER/VOTE,"+ concat_data.decode())
            self.previous_block = None
    

        if encrypt_data: # If it is the first block then there is an Initilization Vector
             self.e_data = encrypt_data

        else:
             self.e_data = None

        if IV:
            self.IV = IV
        else:
            self.IV = get_random_bytes(16) 

        if key:
            self.key = key
        else:
            self.key = get_random_bytes(16)
           

        self.e_cipher = AES.new(self.key, AES.MODE_CBC, self.IV)

        
        if concat_data:
            self.block = self.e_cipher.encrypt(pad(self.data.encode("utf8"), AES.block_size)) #Encrypt the data latin1
        

    def Decrypt_Block(self):
     
    
        # if self.IV:
        #     self.d_cipher = AES.new(self.key, AES.MODE_CBC, self.IV)   
            
             
        # else:
        #     self.d_cipher = AES.new(self.key, AES.MODE_CBC)
        
        
        self.d_cipher = AES.new(self.key, AES.MODE_CBC, self.IV)
          
        if self.e_data:
            decrypted_block = unpad (self.d_cipher.decrypt(self.e_data), AES.block_size)


        return decrypted_block.decode('latin1')

