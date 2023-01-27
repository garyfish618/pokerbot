class PingProcessor()

    def process(self, request):
        # ACK ping coming from discord
            body = request.data
            if body.get('type') == 1:
                self.logger.info("Received PING from Discord")
                return Response({'type': 1}, status=200)
