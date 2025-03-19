import requests
from django.conf import settings

def get_tokens_and_user_info(code):
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    token_resp = requests.post(token_url, data=data).json()
    user_info = {}

    if 'access_token' in token_resp:
        access_token = token_resp['access_token']
        user_info_resp = requests.get(
            'https://www.googleapis.com/oauth2/v2/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        ).json()
        user_info = user_info_resp

    return {"tokens": token_resp, "user_info": user_info}
