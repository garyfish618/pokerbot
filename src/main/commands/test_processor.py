import logging
from rest_framework.response import Response
from .helpers import Helpers

logger = logging.getLogger(__file__)

class TestCommandProcessor():

    @staticmethod
    def process():

        return Helpers.message_response("Hello World")

        

