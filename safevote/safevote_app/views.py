# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from block_chain.AES_Block_Chain import AES_Block_Chain
from block_chain.AES_Block import AES_Block
import requests
# Create your views here.

def add_vote(request):
    e_id, u_id, vote  = request.json()
    new_block = AES_Block(u_id, vote)
    return HttpResponse(response)

def countvotes(request):
    