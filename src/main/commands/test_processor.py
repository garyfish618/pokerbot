import logging
from rest_framework.response import Response
from ..enums.interaction_response_type import InteractionResponseType

logger = logging.getLogger(__file__)

class TestCommandProcessor():

    @staticmethod
    def process():
        json_response = {
            'type': int(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE),
            'data': {
                'content': "Hello World"

            }
        }

        return Response(json_response, status=200)

        

