import logging
from rest_framework.response import Response
from .helpers import Helpers
from ..models import Player

logger = logging.getLogger(__file__)

class CreditsCommandProcessor():

    @staticmethod
    def process_get_credits(user):
        try:
            player = Player.objects.get(user_id=user['id'])
            return Helpers.message_response(f'You have {player.credits} credits!')

        except Player.DoesNotExist:
            return Helpers.message_response(f'You are not registered!')


