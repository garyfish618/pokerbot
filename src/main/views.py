from rest_framework.views import APIView
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from django.http import HttpResponseBadRequest, JsonResponse
from django.conf import settings
from .interactions.ping_processor import PingProcessor
from .interactions.app_command_processor import AppCommandProcessor
from .enums.interaction_type import InteractionType
import logging

class MainPokerBotApiView(APIView):

    def __init__(self):
        self.logger = logging.getLogger(__file__)    

    def post(self, request):
        self.logger.error("LOGGING")
        # Only run verification if not running on local
        if settings.RUNTIME_ENV != 'local':
            response = self.verify_signature(request)
            if isinstance(response, HttpResponseBadRequest):
                self.logger.error("Received an invalid signature. Rejecting")
                return response
        
        elif InteractionType(request.data["type"]) == InteractionType.PING:
            response =  PingProcessor.process(request)

        elif InteractionType(request.data["type"]) == InteractionType.APPLICATION_COMMAND:
            response = AppCommandProcessor.process(request)
        
        else:
            self.logger.error(f'Unknown interaction type with value {request.data["type"]}')
            return(HttpResponseBadRequest(JsonResponse({'errorMessage': 'Unknown interaction'})))  

        # case InteractionType.MESSAGE_COMPONENT:

        # case InteractionType.APPLICATION_COMMAND_AUTOCOMPLETE:

        # case InteractionType.MODAL_SUBMIT:  

        if response == None:
            return(HttpResponseBadRequest(JsonResponse({'errorMessage': 'Unknown interaction' }))) 

        return response       

    def verify_signature(self, request):
        body = request.body.decode('utf-8')
            
        try:
            verify_key = VerifyKey(bytes.fromhex(settings.APP_PUBLIC_KEY))
            signature = request.headers["X-Signature-Ed25519"]
            timestamp = request.headers["X-Signature-Timestamp"]
            
            verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        except (ValueError, BadSignatureError):
            self.logger.error(f'Failed to verify signature: {signature}; timestamp: {timestamp}')
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Invalid request signature'}))
        except KeyError:
            self.logger.error(f'Failed to verify signature: {signature}; timestamp: {timestamp}')
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Missing required headers'}))