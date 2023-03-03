import logging
from rest_framework.response import Response
from .helpers import Helpers
from ..models import Player

logger = logging.getLogger(__file__)

class CreditsCommandProcessor():

    @staticmethod
    def process(user):

        player = Player.objects.get(user_id=user['id'])
        if player == None:
            return Helpers.message_response(f'You are not registered!'), True

        else:
            return Helpers.message_response(f'You have {player["credits"]} credits!')

        

