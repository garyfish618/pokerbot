import logging
from rest_framework.response import Response
from ..commands.test_processor import TestCommandProcessor
from ..commands.register_processor import RegisterCommandProcessor

logger = logging.getLogger(__file__)

class AppCommandProcessor():

    @staticmethod
    def process(request):
        body = request.data['data']
        command_name = body.get('name')
        if command_name == 'test':
            return TestCommandProcessor.process()

        if command_name == 'register':
            return RegisterCommandProcessor.process(request.data['user'])

        else:
            logger.error(f'Unknown command provided with name={command_name}')
            return "Invalid command", False


