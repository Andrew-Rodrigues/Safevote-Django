# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Elections(models.Model):
    election_id = models.CharField(max_length = 250, primary_key = True)

class Candidates(models.Model):
    election = election = models.ForeignKey(Elections, on_delete = models.CASCADE)
    candidate = models.CharField(max_length = 50)

   
class BlockChain (models.Model):
    election = models.ForeignKey(Elections, on_delete = models.CASCADE)
    block_chain = models.TextField() #stores string of block_chain


class Block (models.Model):
    block_chain = models.ForeignKey(BlockChain, on_delete = models.CASCADE)
    data = models.TextField()
    IV = models.CharField(max_length = 16)
    key = models.CharField(max_length = 16)

