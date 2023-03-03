import logging
from rest_framework.response import Response
from ..commands.test_processor import TestCommandProcessor
from ..commands.register_processor import RegisterCommandProcessor
from ..commands.credits_processor import CreditsCommandProcessor

logger = logging.getLogger(__file__)

class AppCommandProcessor():

    @staticmethod
    def process(request):
        body = request.data['data']
        command_name = body.get('name')
        if command_name == 'test':
            return TestCommandProcessor.process()

        if command_name == 'register':
            return RegisterCommandProcessor.process_register(request.data['member']['user'])

        if command_name == 'unregister':
            return RegisterCommandProcessor.process_unregister(request.data['member']['user'])

        if command_name == 'credits':
            return CreditsCommandProcessor.process_get_credits(request.data['member']['user'])

            
        else:
            logger.error(f'Unknown command provided with name={command_name}')
            return "Invalid command", False


