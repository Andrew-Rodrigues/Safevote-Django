# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .block_chain.AES_Block_Chain import AES_Block_Chain
from .block_chain.AES_Block import AES_Block
from Crypto.Hash import HMAC, SHA256

# Create your views here.

def AddVote(request, user_id, vote, hmac):
    
    new_block = AES_Block(user_id.encode(), vote.encode())
    
    return HttpResponse(new_block.Decrypt_Block())


def AddElection(request, election_id, candidates):

    
    return HttpResponse("elections")



def CalculateWinner(request):

    return HttpResponse("Winner")



def index(request):
    return HttpResponse("Block Chain WTF WHERE IS BRANDAN???")

    