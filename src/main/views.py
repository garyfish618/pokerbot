from rest_framework.views import APIView
from rest_framework.response import Response


class MainPokerBotApiView(APIView):

    def post(self, request):
        # ACK ping coming from discord
        if request.data.get('type') == 1:
            return Response({'type': 1}, status=200)
