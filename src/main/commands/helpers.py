from rest_framework.response import Response
from ..enums.interaction_response_type import InteractionResponseType


class Helpers():

    @staticmethod
    def message_response(message):
        return Response({
            'type': int(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE),
            'data': {
                'content': message
            }
        }, status=200)