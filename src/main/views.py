from rest_framework.views import APIView
from rest_framework.response import Response
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from django.http import HttpResponseBadRequest, JsonResponse

class MainPokerBotApiView(APIView):

    def post(self, request):
        body = request.data
        
        try:
            PUBLIC_KEY = '109f9036e7831400d46b3d44b7d3b7e3f837fe3c60e04427dfcf22cb204df8ef'

            print(request.headers)
            verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
            signature = request.headers["X-Signature-Ed25519"]
            timestamp = request.headers["X-Signature-Timestamp"]
            
            print("Attempting signature verification")
            verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
            print("Verified signature")
        except (ValueError, BadSignatureError):
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Invalid request signature'}))
        except KeyError:
            return HttpResponseBadRequest(JsonResponse({'errorMessage': 'Missing required headers'}))
    

        # ACK ping coming from discord
        if body.get('type') == 1:
            print("Got type with 1")
            return Response({'type': 1}, status=200)
