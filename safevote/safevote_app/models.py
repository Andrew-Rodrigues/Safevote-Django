# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class safevote(models.Model):
    user_id = models.CharField(max_length = 50)
    vote = models.CharField(max_length = 50)

    # def __str__(self):
    #     return self.user_id
