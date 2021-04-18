from AES_Block import AES_Block
from AES_Block_Chain import AES_Block_Chain
import hashlib



aes_block = AES_Block("AROID", "TRUMP", IV = "RAHYUTKILLPOLIUH")
aes_block2 = AES_Block("Rod", "Biden", previous_block = aes_block)


aes_block_chain = AES_Block_Chain(aes_block)

aes_block_chain.Add_Block(aes_block2)

aes_block3 = AES_Block("Brandito", "Kanye", previous_block = aes_block_chain.Get_Curr_Block())

aes_block_chain.Add_Block(aes_block3)

yut = aes_block2.Decrypt_Block()

d = aes_block.Decrypt_Block()
rah = aes_block3.Decrypt_Block()

for i in range(10000):

    if ( i % 2 ):
        new_block = AES_Block("ROD", "TRUMP", aes_block_chain.Get_Curr_Block())
        aes_block_chain.Add_Block(new_block)
    else:
        new_block = AES_Block("Brandon", "Kanye" , aes_block_chain.Get_Curr_Block())
        aes_block_chain.Add_Block(new_block)


users, results = aes_block_chain.Calculte_Votes(["Kanye", "TRUMP", "Biden"])

print ("USERS MAP: ", users)
print ("RESULTS MAP: ", results)
print ("Block Cipher Demo: ", "3rd Block in Chain: " , aes_block_chain[3].block)
print ("Block Cipher Demo: " , "3rd Block Decrypted: ", aes_block_chain[3].Decrypt_Block())



