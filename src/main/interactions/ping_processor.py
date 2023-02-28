import logging
from rest_framework.response import Response

logger = logging.getLogger(__file__)

class PingProcessor():

    @staticmethod
    def process(request):
        # ACK ping coming from discord
        body = request.data
        if body.get('type') == 1:
            logger.info("Received PING from Discord")
            return Response({'type': 1}, status=200), True
        
        return "Error processing ping request", False

