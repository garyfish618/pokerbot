import logging
from rest_framework.response import Response
from ..models import Game
from .helpers import Helpers

class GameCommandProcessor():

    @staticmethod
    def process_create_game(guild_id):
        created = Game.objects.get_or_create(guild_id=guild_id)[1]
        return Helpers.message_response(f'Game has been created!') if created else Helpers.message_response(f'There is already a game created for this server. Use /join to join the game!')

    @staticmethod
    def process_start_game(guild_id):
        game = Game.objects.filter(guild_id=guild_id)
        
        if game.started:
            

