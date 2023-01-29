import logging
from rest_framework.response import Response
from ..commands.test_processor import TestCommandProcessor

logger = logging.getLogger(__file__)

class AppCommandProcessor():

    @staticmethod
    def process(request):
        body = request.data['data']
        if body.get('name') == 'test':
            return TestCommandProcessor.process()
            
