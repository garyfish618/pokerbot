import logging
from rest_framework.response import Response
from ..models import Player
from .helpers import Helpers

logger = logging.getLogger(__file__)

class RegisterCommandProcessor():

    @staticmethod
    def process_register(user):
        try:
            player, created = Player.objects.get_or_create(user_id=user['id'])
            if not created:
                return Helpers.message_response(f'@{user["username"]}#{user["discriminator"]} you are already registered!')

            else:
                player.username = user['username']
                player.discriminator = user['discriminator']
                player.save()
                logger.info(f'Registering user with ID={user["id"]} username={user["username"]}#{user["discriminator"]}')
                return Helpers.message_response(f'@{user["username"]}#{user["discriminator"]} you have been registered successfully!')

        except AttributeError as e:
            return "Invalid registration request. Missing fields: " + str(e), False

    @staticmethod
    def process_unregister(user):
        player_deleted = Player.objects.filter(user_id=user['id']).delete()[0]
        
        if player_deleted != 1: 
            return Helpers.message_response(f'You are not registered!')

        else:
            return Helpers.message_response(f'You\'ve been successfully unregistered!') 




    


