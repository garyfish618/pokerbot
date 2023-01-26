from rest_framework.views import APIView
from rest_framework.response import Response
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

class MainPokerBotApiView(APIView):

    def post(self, request):
        PUBLIC_KEY = '109f9036e7831400d46b3d44b7d3b7e3f837fe3c60e04427dfcf22cb204df8ef'

        verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

        signature = request.headers["X-Signature-Ed25519"]
        timestamp = request.headers["X-Signature-Timestamp"]
        body = request.data.decode("utf-8")

        try:
            verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
            print("Verified signature")
        except BadSignatureError:
            abort(401, 'invalid request signature')

        # ACK ping coming from discord
        if request.data.get('type') == 1:
            print("Got type with 1")
            return Response({'type': 1}, status=200)
