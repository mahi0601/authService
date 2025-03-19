from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from urllib.parse import urlencode
from .services.google_auth import get_tokens_and_user_info

# apps/googleauth/views.py

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlencode

class GoogleAuthInitView(APIView):
    def get(self, request):
        base_url = "https://accounts.google.com/o/oauth2/v2/auth"
        params = {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "response_type": "code",
            "scope": "openid email profile https://www.googleapis.com/auth/drive",  # ✅ Add drive scope here
            "access_type": "offline",
            "prompt": "consent",
        }
        auth_url = f"{base_url}?{urlencode(params)}"
        return Response({"auth_url": auth_url})


class GoogleAuthCallbackView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=400)
        data = get_tokens_and_user_info(code)
        return Response(data)


from django.http import JsonResponse

def auth_home(request):
    return JsonResponse({"message": "Welcome to Google OAuth Auth Routes. Try /auth/init"})
