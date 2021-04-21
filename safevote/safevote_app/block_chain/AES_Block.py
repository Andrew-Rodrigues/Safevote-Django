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


    def __init__(self, user_id, vote, previous_block = None, IV = None, key = None):
        # self.key = hashlib.sha256(get_random_bytes(16)).digest() # Each block will have it's own random cipher key
        # self.IV = get_random_bytes(16)

        self.user_id = user_id
        self.vote = vote

        if previous_block: 
            self.previous_block = previous_block
            
            self.data = (previous_block + "USER/VOTE," + user_id+'/'+vote) #Data of block chain is previous_block plus data of new block 
            
        else: #concat_data and previous_block is None:
            self.data = ("USER/VOTE,"+ user_id +'/'+vote)
            self.previous_block = None
    
        # else:

        #     if encrypt_data: 
        #         self.e_data = encrypt_data #.decode()
        #         self.block = None

        #     else:
        #         self.e_data = None


        if IV:
            self.IV = IV
        else:
            self.IV = get_random_bytes(16)

        if key:
            self.key = key
        else:
            self.key = hashlib.sha256(get_random_bytes(16)).digest()

        print(sys.getsizeof(self.IV))    
        self.e_cipher = AES.new(self.key, AES.MODE_CFB, iv = self.IV)
        padded_data = pad(self.data.encode(), AES.block_size)

        self.block = self.e_cipher.encrypt(self.data.encode()).decode('latin1') #Encrypt the data latin1
        

    def Decrypt_Block(self):
       
        self.d_cipher = AES.new(self.key, AES.MODE_CFB, iv = self.IV)
       # padded_data = pad(self.e_data.encode(), AES.block_size)
       

        # decrypted_block = unpad (self.d_cipher.decrypt(self.e_data.encode(), AES.block_size)
        decrypted_block = self.d_cipher.decrypt(self.block.encode())

        # if self.block:
        #     decrypted_block = unpad (self.d_cipher.decrypt(self.block), AES.block_size)

        return decrypted_block.decode('latin1')

