# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from .block_chain.AES_Block_Chain import AES_Block_Chain
from .block_chain.AES_Block import AES_Block
from Crypto.Hash import HMAC, SHA256
from .models import Elections, Candidates, Block

# Create your views here.

#FUNCTION THAT DETERMINES IF DATA COMING IN IS AUTHENTIC 
def CheckHMAC(hmac, data):
    secret_key = "ANDREWBRANDONDANIELKENNETH".encode()
    h = HMAC.new(secret_key, digestmod=SHA256)
    h.update(data)

    try:
        h.hexverify(hmac)
        print("Data is authentic")
    except ValueError:
        print("Data has been tampered with")
        return False

    return True

def AddVote(request, election_id, user_id, vote, hmac):

    data = (election_id+user_id + vote).encode()

    if(not CheckHMAC(hmac, data)):
        return HttpResponse(403)

    #GET ELECTION AND GET LAST ADDED BLOCK
    try:
        election = Elections.objects.get(election_id = election_id)
    except:
        print("ERROR QUERYING: ELECTION DOESN'T EXIST")
        return HttpResponse(500)
    #try:
    previous_block = Block.objects.last()
    #except:
    print("ERROR QUERYING: PREVIOUS BLOCK")
        #return HttpResponse(500)

    
    #CREATE NEW BLOCK USING BLOCK CHAIN API

    # concat_data = user_id + "/" + vote
    new_block = AES_Block(user_id, vote, previous_block = previous_block.data)
    #ADD NEW BLOCK TO DATABASE and BUILD BLOCK
    add_block = Block.objects.create(
        election = election,
        index = (previous_block.index + 1),
        data = new_block.block,
        user_id = new_block.user_id,
        vote = new_block.vote,
        IV = new_block.IV,
        key = new_block.key,
     )
    
    return HttpResponse(200)


def AddElection(request, election_id, candidates, hmac):

    data = election_id

    list_candidates = candidates.split('-')
   
    for cand in list_candidates:
        data += cand   

    if (not CheckHMAC(hmac,data.encode())):
        return HttpResponse(403)
        

    #CREATE ELECTION
    try:
        newElection = Elections.objects.create(election_id = election_id)
        newElection.save()
    except:
        print('ELECTION NOT ADDED')     
        return HttpResponse(500)


    #INIT GENISIS BLOCK TO DB
    #try:
    gen_block = AES_Block("Election", election_id)
    newBlock = Block.objects.create(election = newElection, index = 0, user_id = gen_block.user_id, vote = gen_block.vote, data = gen_block.block, IV = gen_block.IV, key = gen_block.key) 
    newBlock.save()
    #except:
    print('GENISIS BLOCK NOT ADDED')
        #return HttpResponse(500)

    #ADD CANDIDATES TO DB
    try:
        for cand in list_candidates:
            newCandidate = Candidates.objects.create(election = newElection, candidate = cand)
    except:
        print('CANDIDATES NOT ADDED')
        return HttpResponse(500)

    return HttpResponse(200)



def CalculateElection(request, election_id, hmac):

    if (not CheckHMAC(hmac,election_id.encode())):
        return HttpResponse(403)

    try:
        e = Elections.objects.get(election_id = election_id)
    except:
        print("ERROR: QUERYING: ELECTION DOESN'T EXIST")
        return HttpResponse(500)

    try:
        cands = e.candidates_set.all()
    except:
        print("ERROR QUERYING: ALL CANDIDATES")
        return HttpResponse(500)
        
    try:
        blocks = e.block_set.all()
    except:
        print("ERROR QUERYING: ALL BLOCKS")
        return HttpResponse(500)

    #BUILD BLOCKCHAIN OBJECT WITH BLOCK CHAIN API
    list_cands = []
    for c in cands:
        list_cands.append(c.candidate)
    
    gen_block = AES_Block(blocks[0].user_id, blocks[0].vote, IV = blocks[0].IV, key = blocks[0].key)
    block_chain = AES_Block_Chain(gen_block)


    blocks = blocks[1:]

    for block in blocks:
        create_block = AES_Block(block.user_id, block.vote, IV = block.IV, key = block.key)
        block_chain.Add_Block(create_block)

    results = block_chain.Calculte_Votes(list_cands)

    vote_count = results[list_cands[0]]
    winner = list_cands[0]
    new_cands = list_cands[0:]
    tie = True

    for c in new_cands:
        if(vote_count  < results[c]):
            tie = False
            vote_count = results[c]
            winner = c 
    if not tie:
        data = {
            'winner': winner,
            'vote count' : vote_count
        }
    else:
        winner = "Tie"
        data = {
            'winner' : winner,
            'vote count' : vote_count
        }

    #dump = json.dumps(data)

    return JsonResponse(data)



def DeleteElection(request, election_id, hmac):

    if(not CheckHMAC(hmac, election_id.encode())):
        return HttpResponse(403)

    try:
        e = Elections.objects.get(election_id = election_id)
    except:
        print("ERROR QUERYING: ELECTION DOESN'T EXIST")
        return HttpResponse(500)

    #DELTES ELECTION AND ALL CANDIDATES AND BLOCKCHAIN THROUGH CASCADE
    try:
        e.delete()
    except:
        print("ERROR DELETING ELECTION")
        return HttpResponse(500)
    

    return HttpResponse(200)



def index(request):
    return HttpResponse("Block Chain!!!")

def TestDB(request):
    e = Elections.objects.get(election_id = "12345")
    c = Candidates.objects.get(election = "12345", candidate = 'Biden')
    b = Block.objects.get(election = "12345", index = 0)
    
    block = AES_Block(encrypt_data = b.data, IV = b.IV, key = b.key )
    print(block.Decrypt_Block())

    return HttpResponse("TEST DB")

    