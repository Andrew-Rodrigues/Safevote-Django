# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Elections(models.Model):
    election_id = models.CharField(max_length = 250, primary_key = True)

class Candidates(models.Model):
    election = models.ForeignKey(Elections, on_delete = models.CASCADE)
    candidate = models.CharField(max_length = 50, primary_key = True)

   
# class BlockChain (models.Model):
#     election = models.OneToOneField(Elections, on_delete = models.CASCADE)
#     block_chain = models.TextField() #stores string of block_chain


class Block (models.Model):
    election = models.ForeignKey(Elections, on_delete = models.CASCADE)
    index = models.IntegerField(default = 0, primary_key = True)
    user_id = models.CharField(max_length = 50, default='Andrew')
    vote = models.CharField(max_length = 50, default='Trump')
    data = models.TextField()
    IV = models.BinaryField(max_length = 16)
    key = models.BinaryField(max_length = 16)

