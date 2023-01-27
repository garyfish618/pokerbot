from rest_framework.views import APIView
from rest_framework.response import Response
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from django.http import HttpResponseBadRequest, JsonResponse
from django.conf import settings
import logging

class MainPokerBotApiView(APIView):

    def __init__(self):
        self.logger = logging.getLogger(__file__)    

    def post(self, request):

        # Only run verification if not running on local
        if settings.RUNTIME_ENV != 'local':
            response = self.verify_signature(request)
            if isinstance(response, HttpResponseBadRequest):
                self.logger.error("Received an invalid signature. Rejecting")
                return response

        


    def verify_signature(self, request):
        body = request.body.decode('utf-8')
            
        try:
            verify_key = VerifyKey(bytes.fromhex(settings.APP_PUBLIC_KEY))
            signature = request.headers["X-Signature-Ed25519"]
            timestamp = request.headers["X-Signature-Timestamp"]
            
            verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        except (ValueError, BadSignatureError):
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Invalid request signature'}))
        except KeyError:
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Missing required headers'}))