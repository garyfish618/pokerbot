import logging
from rest_framework.response import Response
from ..commands.test_processor import TestCommandProcessor

logger = logging.getLogger(__file__)

class AppCommandProcessor():

    @staticmethod
    def process(request):
        body = request.data['data']
        command_name = body.get('name')
        if command_name == 'test':
            return TestCommandProcessor.process()

        else:
            logger.error(f'Unknown command provided with name={command_name}')
            

            
