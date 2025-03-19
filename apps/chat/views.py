from rest_framework.views import APIView
from rest_framework.response import Response

class ChatTestView(APIView):
    def get(self, request):
        return Response({"message": "Chat WebSocket is working!"})
