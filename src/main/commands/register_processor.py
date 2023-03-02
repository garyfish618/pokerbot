import logging
from rest_framework.response import Response
from ..models import Player
from .helpers import Helpers

logger = logging.getLogger(__file__)

class RegisterCommandProcessor():

    @staticmethod
    def process(user, nickname=None):
        try:
            player, created = Player.objects.get_or_create(user_id=user['id'])
            print(created)
            if not created:
                return Helpers.message_response(f'@<{user["id"]}> you are already registered!'), True

            else:
                player.username = user['username']
                player.discriminator = user['discriminator']
                player.save()
                logger.info(f'Registering user with ID={user["id"]} username={user["username"]}#{user["discriminator"]}')
                return Helpers.message_response(f'@{user["username"]}#{user["discriminator"]} you have been registered successfully!'), True

        except AttributeError as e:
            return "Invalid registration request. Missing fields: " + str(e), False



    


