from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=80)

class Player(models.Model):
    nick_name = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=64)
    discriminator = models.CharField(max_length=4)
    credits = models.IntegerField(default=0)

class Game(models.Model):
    guild_id = models.CharField(max_length=64, unique=True)
    started = models.BooleanField(default=False)
    credit_pot = models.IntegerField(default=0)
    
    